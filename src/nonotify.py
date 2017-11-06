import xchat
import re
__module_name__ = 'No Notify'
__module_version__ = '1'
__module_description__ = 'Eat Notifcations'


channel_list = list()
green = '\x02\x0303'
red = '\x02\x0304'


def on_unload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (green, __module_name__))


def nonotify_callback(word):
    if xchat.get_info("channel") in channel_list:
        xchat.emit_print('Channel Message','%s%s' % (red, word[0]),'%s%s' % (red,word[1]))
        return xchat.EAT_ALL
    else:
        return xchat.EAT_NONE


def remove_nonotify(channel):
    if channel in channel_list:
        xchat.prnt('%sNoNotify - Removing %s from NoNotify channel list.' % (green, channel))
        channel_list.remove(channel)
    else:
        xchat.prnt('%sNoNotify - Not removing %s - not in list.' % (green, channel))
    return xchat.EAT_ALL


def nonotify(word,word_eol,userdata):
    if word[1] == 'show':
        return show_nonotify()
    if word[1] == 'remove':
        return remove_nonotify(word[2])
    channels = re.split('(?:,|\s)+',word_eol[1])
    for channel in channels:
        if channel not in channel_list:
           xchat.prnt('%sNoNotify - Adding %s to NoNotify channel list.' % (green, channel))
           channel_list.append(channel)
        else:
           xchat.prnt('%sNoNotify -  Not adding %s, already in NoNotify channel list.' % (green,channel))
    return xchat.EAT_ALL


def show_nonotify():
    if not channel_list:
        xchat.prnt('%sNoNotify - The NoNotify list is empty.' % green)
    else:
        xchat.prnt('%sNoNotify - The following channels are on the NoNotify list:' % green)
        for channel in channel_list:
            xchat.prnt('%s    - %s' % (green, channel))
    return xchat.EAT_ALL

xchat.hook_print('Channel Msg Hilight', nonotify_callback)
xchat.hook_print('Channel Action Hilight', nonotify_callback)
xchat.hook_command('nonotify', nonotify)
xchat.hook_unload(on_unload)

xchat.prnt('%sModule No Notify Loaded.' % green)

