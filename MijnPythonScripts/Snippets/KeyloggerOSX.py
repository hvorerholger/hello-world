# cocoa_keypress_monitor.py by Bjarte Johansen is licensed under a 
# License: http://ljos.mit-license.org/
 
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
 
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)
 
def handler(event):
    try:
        NSLog(u"%@", event)
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()
 
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    main()
