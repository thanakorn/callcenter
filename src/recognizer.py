__author__ = 'thanakorn'

import pygtk
pygtk.require('2.0')
import gtk

import gobject
import pygst
pygst.require('0.10')
gobject.threads_init()
import gst
import os


class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update()


class SpeechRecognizer(Subject):
    """ GStreamer based speech recognizer. """

    def __init__(self):
        """ Initialize the speech pipeline components. """
        # configure pipeline
        Subject.__init__(self)
        self.input = ''
        self.pipeline = gst.parse_launch('gconfaudiosrc ! audioconvert ! audioresample '
                                         + '! vader name=vad auto-threshold=true '
                                         + '! pocketsphinx name=asr ! fakesink')

        asr = self.pipeline.get_by_name('asr')
        asr.connect('partial_result', self.asr_partial_result)
        asr.connect('result', self.asr_result)
        asr.set_property('configured', True)
        asr.set_property('dsratio', 1)

        # parameters for grammar and dic
        grammar = os.getcwd() + '/pocketsphinx_config/callcenter.fsg'
        dic = os.getcwd() + '/pocketsphinx_config/callcenter.dic'
        asr.set_property('fsg', grammar)
        asr.set_property('dict', dic)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message::application', self.application_message)

    def shutdown(self):
        """ Shutdown the GTK thread. """
        gtk.main_quit()

    def start(self):
        self.pipeline.set_state(gst.STATE_PLAYING)
        gtk.main()

    def stop(self):
        self.pipeline.set_state(gst.STATE_PAUSED)

    def resume(self):
        self.pipeline.set_state(gst.STATE_PLAYING)

    def asr_partial_result(self, asr, text, uttid):
        """ Forward partial result signals on the bus to the main thread. """
        struct = gst.Structure('partial_result')
        struct.set_value('hyp', text)
        struct.set_value('uttid', uttid)
        asr.post_message(gst.message_new_application(asr, struct))

    def asr_result(self, asr, text, uttid):
        """ Forward result signals on the bus to the main thread. """
        struct = gst.Structure('result')
        struct.set_value('hyp', text)
        struct.set_value('uttid', uttid)
        asr.post_message(gst.message_new_application(asr, struct))

    def application_message(self, bus, msg):
        """ Receive application messages from the bus. """
        msgtype = msg.structure.get_name()
        if msgtype == 'partial_result':
            self.partial_result(msg.structure['hyp'], msg.structure['uttid'])
        if msgtype == 'result':
            self.final_result(msg.structure['hyp'], msg.structure['uttid'])

    def partial_result(self, hyp, uttid):
        """ Delete any previous selection, insert text and select it. """
        print('Partial: ' + hyp)

    def final_result(self, hyp, uttid):
        """ Insert the final result. """
        print('Final: ' + hyp)
        self.input = hyp
        for observer in self._observers:
            observer.update()

    def get_final_result(self):
        return self.input

if __name__=="__main__":
    recognizer = SpeechRecognizer()
