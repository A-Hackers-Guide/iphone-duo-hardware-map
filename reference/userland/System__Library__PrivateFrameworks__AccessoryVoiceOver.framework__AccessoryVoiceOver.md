# `/System/Library/PrivateFrameworks/AccessoryVoiceOver.framework/AccessoryVoiceOver`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 2 classes, 3 protocols, 65 methods, 11 properties

### Class pages

Every class and protocol, with its methods: [`ACCVoiceOverAccessory`](../objc/ACCVoiceOverAccessory_AccessoryVoiceOver.md), [`ACCVoiceOverProvider`](../objc/ACCVoiceOverProvider_AccessoryVoiceOver.md), [`ACCVoiceOverXPCClientProtocol`](../objc/ACCVoiceOverXPCClientProtocol_AccessoryVoiceOver.protocol.md), [`ACCVoiceOverXPCServerProtocol`](../objc/ACCVoiceOverXPCServerProtocol_AccessoryVoiceOver.protocol.md), [`NSObject`](../objc/NSObject_AccessoryVoiceOver.protocol.md)

### Classes

`ACCVoiceOverAccessory`, `ACCVoiceOverProvider`

### Protocols

`ACCVoiceOverXPCClientProtocol`, `ACCVoiceOverXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (TB,N,V_desiredVoiceOverState) desiredVoiceOverState;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCVoiceOverXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"<ACCVoiceOverProviderProtocol>",W,N,V_delegate) delegate;
```

## Strings (112)

```
ACCVoiceOverActionParameterScaleKey
ACCVoiceOverActionParameterTouchTypeKey
ACCVoiceOverCursorInformationUpdateTraitsKey
com.apple.accessories.voiceover.availability-changed
com.apple.accessories.voiceover
ACCVoiceOverActionParameterPointYKey
ACCVoiceOverActionParameterTextKey
ACCVoiceOverCursorInformationUpdateFrameKey
v16@?0@\"NSError\"8
null
_SetupAvailabilityChangedHandlerForServiceEntry
ACCVoiceOverCursorInformationUpdateFrameTopYKey
Transport
ACCVoiceOverInformationUpdateSpeakingRateKey
ACCVoiceOverInformationUpdateContextKey
ACCVoiceOverCursorInformationUpdateValueKey
ACCVoiceOverCursorInformationUpdateContextKey
<Undefined>
v8@?0
com.apple.accessories.signposts
ACCVoiceOverInformationUpdateSpeakingVolumeKey
ACCVoiceOverCursorInformationUpdateLabelKey
ACCVoiceOverCursorInformationUpdateFrameBottomXKey
General
Connection
v12@?0B8
ACCVoiceOverInformationUpdateEnabledKey
Endpoint
ACCVoiceOverCursorInformationUpdateFrameTopXKey
accessoryServer_isServerAvailableForServiceEntry
v12@?0i8
ACCVoiceOverCursorInformationUpdateFrameBottomYKey
com.apple.accessories.frameworks
ACCVoiceOverCursorInformationUpdateHintKey
ACCVoiceOverActionParameterPointXKey
ACCVoiceOverProvider connectToServer, _providerUID=%@, IS accessoryServer_isServerAvailable()
accessoryVoiceOverDetachAll: notify detach of %lu accessories!
accessoryVoiceOver: %@ setContext: %d, accessory does not exist!
accessoryVoiceOver: %@ requestConfiguration: %d param: %@, delegate does not respond to selector %@
accessoryVoiceOverStartInformationUpdate %@
accessoryVoiceOverStopCursorInformationUpdate %@
Call initConnection to remoteObject=%@
accessoryVoiceOverStopCursorInformationUpdate: %@, accessory=%@
updateVoiceOverInfo: %@, _providerUID=%@ _remoteObject=%@
updateVoiceOverInfo: %@, _remoteObject nil, _providerUID=%@
updateVoiceOverCursorInfo: %@, _providerUID=%@ _remoteObject=%@
Register AvailabilityChangedHandler (%d, %s)
%s (%d)
accessoryVoiceOverStartInformationUpdate: %@, accessory does not exist!
accessoryVoiceOverStartCursorInformationUpdate: %@, delegate does not respond to selector %@
accessoryVoiceOverStopCursorInformationUpdate: %@, accessory does not exist! _accessories=%@
accessoryVoiceOverDetached: accessory %@ _accessories=%@
Unregister AvailabilityChangedHandler (%d, %s)
ACCVoiceOverProvider connectToServer, _providerUID=%@
accessoryVoiceOverDetached: accessory %@, accessory=%@
accessoryVoiceOver: %@ setContext: %d, accessory does not exist! _accessories=%@
accessoryVoiceOver: %@ performAction: %d parameters: %@, delegate does not respond to selector %@
accessoryVoiceOverStopInformationUpdate: %@, accessory does not exist! _accessories=%@
XPC connection invalidated!
accessoryVoiceOver: %@ setEnabled: %d, accessory=%@
accessoryVoiceOverStopCursorInformationUpdate: %@, delegate does not respond to selector %@
accessoryVoiceOverStopCursorInformationUpdate: %@, accessory does not exist!
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Getting remote object...
accessoryVoiceOverAttached: accessory %@ (%@) already exists!
accessoryVoiceOverDetachAll: accessory %@
accessoryVoiceOver: %@ performAction: %d parameters: %@, accessory does not exist!
accessoryVoiceOverStartInformationUpdate: %@, accessory=%@
%s (%d, %s)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
accessoryVoiceOverAttached: accessory %@, accessory=%@
accessoryVoiceOver: %@ setContext %d, accessory=%@
accessoryVoiceOverDetached: accessory %@ (%@) does not exist!
accessoryVoiceOver: %@ performAction: %d parameters: %@, accessory does not exist! _accessories=%@
accessoryVoiceOver: %@ requestConfiguration: %d param: %@, accessory=%@
accessoryVoiceOverStopInformationUpdate: %@, accessory does not exist!
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
XPC connection interrupted!
%@
accessoryVoiceOver: %@ setContext: %d, delegate does not respond to selector %@
accessoryVoiceOver: %@ performAction: %d parameters: %@, accessory=%@
accessoryVoiceOver: %@ requestConfiguration: %d param: %@, accessory does not exist!
%s cannot get server state (%d, %s)
%s did not register for notification (%d, %s), token (%d)
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created log object %s: %s
Failed to create os_log_t object %s: %s!
ACCVoiceOverProvider init, _providerUID=%@
accessoryVoiceOver: %@ requestConfiguration: %d param: %@, accessory does not exist! _accessories=%@
accessoryVoiceOverStartInformationUpdate: %@, accessory does not exist! _accessories=%@
accessoryVoiceOverStopInformationUpdate %@
accessoryVoiceOverStopInformationUpdate: %@, accessory=%@
accessoryVoiceOverStopInformationUpdate: %@, delegate does not respond to selector %@
Created %d log object(s)!
shouldStayConnected: %d
accessoryVoiceOver: %@ setEnabled: %d, accessory does not exist!
accessoryVoiceOverStartCursorInformationUpdate: %@, accessory does not exist!
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Trying to connect to server...
ACCVoiceOverProvider connectToServer, _providerUID=%@, NOT accessoryServer_isServerAvailable()
Server availability changed! State: %d
Connecting to XPC server...
accessoryVoiceOver: %@ setEnabled: %d, accessory does not exist! _accessories=%@
accessoryVoiceOverStartCursorInformationUpdate: %@, accessory=%@
updateVoiceOverCursorInfo: %@, _remoteObject nil _providerUID=%@
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
accessoryVoiceOverAttached: accessory %@ _accessories=%@
accessoryVoiceOver: %@ setEnabled: %d, delegate does not respond to selector %@
accessoryVoiceOverStartCursorInformationUpdate %@
accessoryVoiceOverStartCursorInformationUpdate: %@, accessory does not exist! _accessories=%@
XPC connection error!
accessoryVoiceOverStartInformationUpdate: %@, delegate does not respond to selector %@
```
