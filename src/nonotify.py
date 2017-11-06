import xchat

__module_name__ = 'No Notify'
__module_version__ = '1'
__module_description__ = 'Eat Notifcations'


channel_list = list()
green = '\x02\x0303'
red = '\x02\x0304'


def on_unload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (green, __module_name__))


def nonotify_callback(word, word_eol, user_data):
    if xchat.get_info("channel") in channel_list:
        xchat.emit_print('Channel Message','%s%s' % (red, word[0]),'%s%s' % (red,word[1]))
        return xchat.EAT_ALL
    else:
        return xchat.EAT_NONE


def remove_nonotify(word,word_eol,userdata):
    if len(word) > 2 and word[2] in channel_list:
        xchat.prnt('%sNoNotify - Removing %s from no notify channel list.' % (green, word[2]))
        channel_list.remove(word[2])
    else:
        xchat.prnt('%sNoNotify - Not removing %s - not in list.' % (green, word[2]))


def nonotify(word,word_eol,userdata):
    if word[1] == 'show':
        return show_nonotify(word,word_eol,userdata)
    if word[1] == 'remove':
        return remove_nonotify(word,word_eol,userdata)
    if word[1] not in channel_list:
        xchat.prnt('%sNoNotify - Adding %s to no notify channel list.' % (green, word[1]))
        channel_list.append(word[1])
    else:
        xchat.prnt('%sNoNotify -  Not adding %s, already in no notify channel list.' % (green,word[1]))


def show_nonotify(word,word_eol,userdata):
    if not channel_list:
        xchat.prnt('%sNoNotify - The NoNotify list is empty.' % green)
    else:
        xchat.prnt('%sNoNotify - The following channels are on the NoNotify list:' % green)
        for channel in channel_list:
            xchat.prnt('%s    - %s' % (green, channel))

xchat.hook_print('Channel Msg Hilight', nonotify_callback)
xchat.hook_print('Channel Action Hilight', nonotify_callback)
xchat.hook_command('nonotify', nonotify)
xchat.hook_unload(on_unload)

xchat.prnt('%sModule No Notify Loaded.' % green)
