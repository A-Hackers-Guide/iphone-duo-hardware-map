# `ATAudioSessionClientImpl`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 5 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"AVAudioSession" _weakSession;
@"AVAudioSession" _strongSession;
@"ATAudioSessionPropertyManager" _propertyManager;
{unique_ptr<AudioSessionPropertyListeners, std::default_delete<AudioSessionPropertyListeners>>=""{?="__ptr_"^{AudioSessionPropertyListeners}}} _propertyListeners;
{map<std::string, std::shared_ptr<OldNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>="__tree_"{__tree<std::__value_type<std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::__map_value_compare<std::string, std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<OldNotificationCenterObserver>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _oldNotificationCenterObservers;
{map<std::string, std::shared_ptr<NewNotificationCenterObserver>, std::less<std::string>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>="__tree_"{__tree<std::__value_type<std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::__map_value_compare<std::string, std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::shared_ptr<NewNotificationCenterObserver>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _newNotificationCenterObservers;
{ObjectRef<__CFRunLoop *>="mCFObject"^{__CFRunLoop}} _clientRunLoop;
{StringRef="mObject"{ObjectRef<const __CFString *>="mCFObject"^{__CFString}}} _clientRunLoopMode;
B _isConfigured;
I _interruptionType;
^? _clientInterruptionListenerProc;
^v _clientUserData;
```

## Properties

```
@property (T^?,V_clientInterruptionListenerProc) clientInterruptionListenerProc;
@property (T^v,V_clientUserData) clientUserData;
@property (TB,V_isConfigured) isConfigured;
@property (T@"AVAudioSession",R) avas;
@property (TI,V_interruptionType) interruptionType;
```

## Instance methods

```
-[ATAudioSessionClientImpl observeValueForKeyPath:ofObject:change:context:];
-[ATAudioSessionClientImpl isValid];
-[ATAudioSessionClientImpl initWithSession:];
-[ATAudioSessionClientImpl handleInterruption:];
-[ATAudioSessionClientImpl isConfigured];
-[ATAudioSessionClientImpl AudioSessionGetPropertyImpl:size:data:];
-[ATAudioSessionClientImpl AudioSessionRemovePropertyListenerImpl:];
-[ATAudioSessionClientImpl AudioSessionSetActiveImpl:flags:];
-[ATAudioSessionClientImpl AudioSessionAddPropertyListenerImpl:userProc:userData:];
-[ATAudioSessionClientImpl AudioSessionGetPropertySizeImpl:size:];
-[ATAudioSessionClientImpl AudioSessionRemovePropertyListenerWithUserDataImpl:userProc:userData:];
-[ATAudioSessionClientImpl AudioSessionSetPropertyImpl:size:data:];
-[ATAudioSessionClientImpl addAVAudioSessionKVOObservers:session:];
-[ATAudioSessionClientImpl addNSNotificationListenerFor:session:block:];
-[ATAudioSessionClientImpl addNSNotificationListenerFor:session:selector:];
-[ATAudioSessionClientImpl avas];
-[ATAudioSessionClientImpl callPropertyListeners:data:];
-[ATAudioSessionClientImpl clientInterruptionListenerProc];
-[ATAudioSessionClientImpl clientUserData];
-[ATAudioSessionClientImpl handleRouteChange:];
-[ATAudioSessionClientImpl handleServerDeath:];
-[ATAudioSessionClientImpl handleServerReset:];
-[ATAudioSessionClientImpl initWithStrongSession:];
-[ATAudioSessionClientImpl interruptionType];
-[ATAudioSessionClientImpl removeAVAudioSessionKVOObservers:];
-[ATAudioSessionClientImpl resetClientConfiguration];
-[ATAudioSessionClientImpl setClientConfiguration:runLoopMode:listenerProc:userData:];
-[ATAudioSessionClientImpl setClientInterruptionListenerProc:];
-[ATAudioSessionClientImpl setClientUserData:];
-[ATAudioSessionClientImpl setInterruptionType:];
-[ATAudioSessionClientImpl setIsConfigured:];
```
