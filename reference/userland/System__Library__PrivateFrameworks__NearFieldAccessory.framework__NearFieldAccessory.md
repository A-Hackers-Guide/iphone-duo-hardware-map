# `/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory`

iOS 27.2 dyld shared cache image. Version `371.8.0.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libnfshared.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 8 classes, 12 protocols, 173 methods, 39 properties

### Class pages

Every class and protocol, with its methods: [`NFACTag`](../objc/NFACTag_NearFieldAccessory.protocol.md), [`NFACTag`](../objc/NFACTag_NearFieldAccessory.md), [`NFAccessoryHardwareManager`](../objc/NFAccessoryHardwareManager_NearFieldAccessory.md), [`NFAccessoryReaderSession`](../objc/NFAccessoryReaderSession_NearFieldAccessory.md), [`NFAccessorySession`](../objc/NFAccessorySession_NearFieldAccessory.protocol.md), [`NFAccessorySession`](../objc/NFAccessorySession_NearFieldAccessory.md), [`NFHardwareManagerAccessoryCallbacks`](../objc/NFHardwareManagerAccessoryCallbacks_NearFieldAccessory.protocol.md), [`NFHardwareManagerAccessoryCallbacks`](../objc/NFHardwareManagerAccessoryCallbacks_NearFieldAccessory.md), [`NFHardwareManagerAccessoryInterface`](../objc/NFHardwareManagerAccessoryInterface_NearFieldAccessory.protocol.md), [`NFHardwareManagerAccessoryInterface`](../objc/NFHardwareManagerAccessoryInterface_NearFieldAccessory.md), [`NFReaderSessionAccessoryCallbacks`](../objc/NFReaderSessionAccessoryCallbacks_NearFieldAccessory.protocol.md), [`NFReaderSessionAccessoryCallbacks`](../objc/NFReaderSessionAccessoryCallbacks_NearFieldAccessory.md), [`NFReaderSessionAccessoryInterface`](../objc/NFReaderSessionAccessoryInterface_NearFieldAccessory.protocol.md), [`NFReaderSessionAccessoryInterface`](../objc/NFReaderSessionAccessoryInterface_NearFieldAccessory.md), [`NFSessionAccessoryCallbackInterface`](../objc/NFSessionAccessoryCallbackInterface_NearFieldAccessory.protocol.md), [`NFSessionAccessoryInterface`](../objc/NFSessionAccessoryInterface_NearFieldAccessory.protocol.md), [`NFXPCServiceClientDelegate`](../objc/NFXPCServiceClientDelegate_NearFieldAccessory.protocol.md), [`NSCoding`](../objc/NSCoding_NearFieldAccessory.protocol.md), [`NSObject`](../objc/NSObject_NearFieldAccessory.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_NearFieldAccessory.protocol.md)

### Classes

`NFACTag`, `NFAccessoryHardwareManager`, `NFAccessoryReaderSession`, `NFAccessorySession`, `NFHardwareManagerAccessoryCallbacks`, `NFHardwareManagerAccessoryInterface`, `NFReaderSessionAccessoryCallbacks`, `NFReaderSessionAccessoryInterface`

### Protocols

`NFACTag`, `NFAccessorySession`, `NFHardwareManagerAccessoryCallbacks`, `NFHardwareManagerAccessoryInterface`, `NFReaderSessionAccessoryCallbacks`, `NFReaderSessionAccessoryInterface`, `NFSessionAccessoryCallbackInterface`, `NFSessionAccessoryInterface`, `NFXPCServiceClientDelegate`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TI,R,N) type;
@property (TI,R,N) technology;
@property (TB,R,N) isSilent;
@property (TC,R,N) silentType;
@property (T@"NSData",R,C,N) tagID;
@property (T@"NSData",R,C,N) UID;
@property (TI,R,N) ndefAvailability;
@property (TQ,R,N) ndefMessageSize;
@property (TQ,R,N) ndefContainerSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (TI,R,N) type;
@property (TI,R,N) technology;
@property (TB,R,N) isSilent;
@property (TC,R,N) silentType;
@property (T@"NSData",R,C,N) tagID;
@property (T@"NSData",R,C,N) UID;
@property (TI,R,N) ndefAvailability;
@property (TQ,R,N) ndefMessageSize;
@property (TQ,R,N) ndefContainerSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<NFAccessoryReaderSessionDelegate>",W) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,V_state) state;
@property (TB,R) didEnd;
@property (TB,R) isActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (186)

```
MiFare UL
MiFare DESFire
v24@?0@\"NSError\"8@\"NSData\"16
Unknown
nfac.fwk
%s:%i Failed to update HW support: %@
com.apple.NFAccessory.session
-[NFAccessoryReaderSession checkNdefSupport:andWrite:error:]_block_invoke
%s
-[NFAccessorySession _endProxySession]_block_invoke
sak
-[NFAccessoryReaderSession readNDEF:]_block_invoke
No connection to nfcacd
v24@?0@\"NSData\"8@\"NSError\"16
-[NFAccessoryHardwareManager setClientName:onConnection:]_block_invoke
%s:%i Unexpected connectionID (%lu vs %lu); dropping request
%s:%i Failed to get HW support : No XPC connection
-[NFAccessoryReaderSession(InternalTest) sendMFGCommand:payload:error:]_block_invoke
v8@?0
atqa
A
v24@?0@8^B16
com.apple.nfcacd.hwmanager
-[NFAccessoryHardwareManager pushSignedRF:]_block_invoke
-[NFAccessoryHardwareManager updateHWSupport:error:]_block_invoke
-[NFAccessoryReaderSession connectTag:error:]_block_invoke
Method
v12@?0I8
%s:%i Bad State
Session ended before started.
type
MiFare
-[NFAccessoryReaderSession didTerminate:]
-[NFAccessoryHardwareManager didInvalidate:]
v24@?0@\"NSObject<NFReaderSessionAccessoryInterface>\"8@\"NSError\"16
-[NFAccessoryHardwareManager enableLPCD:]_block_invoke
-[NFAccessorySession remoteObjectProxyWithErrorHandler:]
MiFare Plus
-[NFAccessoryHardwareManager didInterrupt:connectionID:]
-[NFAccessoryHardwareManager startReaderSession:]_block_invoke_2
%s:%i no proxy available
%s:%i %{public}@
-[NFAccessoryReaderSession readTypeIdentifier:]_block_invoke
%s:%i Connection has refreshed
-[NFAccessoryHardwareManager restartMultiTag]_block_invoke
-[NFAccessoryHardwareManager clearMultiTagState]_block_invoke
PMm
-[NFAccessoryReaderSession startPollingForTechnology:error:]_block_invoke
-[NFAccessoryReaderSession disconnectTag:]_block_invoke
%s:%i Error = %{public}@
-[NFAccessoryHardwareManager updateHWSupport:error:]
technology
Felica
%s:%i API has been deprecated!!!!
-[NFAccessoryReaderSession setTagDataRate:]_block_invoke
%s:%i HW is not supported on this platform
%s:%i Retrying xpc connection - proxy error: %{public}@
-[NFAccessoryHardwareManager getDieId:]_block_invoke
%s:%i session ended
I
allSystemCodes
Hardware is not supported
-[NFAccessoryHardwareManager enableMultiTag:]_block_invoke
-[NFAccessoryHardwareManager getPowerCounters:]_block_invoke
%s:%i endSession should have been called before dealloc
silentType
Generic 4B
%s:%i started=%{public}@ 
-[NFAccessoryHardwareManager triggerDelayedWake:]_block_invoke
-[NFAccessorySession endSessionWithCompletion:]
AppData
%s:%i Invalid connection, retry...
v16@?0@8
v24@?0@\"NSDictionary\"8@\"NSError\"16
Generic 4A
-[NFAccessoryReaderSession transceive:error:]_block_invoke
-[NFAccessoryHardwareManager init]
%s:%i XPC Failure: %{public}@
%s:%i 
v16@?0@\"NSError\"8
ISO15693
MiFare Classic
%s:%i Session has terminated due to: %{public}@
v24@?0B8B12@\"NSError\"16
-[NFAccessoryHardwareManager getMultiTagState:]_block_invoke
-[NFAccessoryReaderSession startPolling:]_block_invoke
nfcd
Generic 3A
-[NFAccessoryHardwareManager _connectIfNeeded:]
-[NFAccessoryHardwareManager getInfo]_block_invoke
identifier
%@-%@ { Tech=%@ Type=%@ silentType=%d ID=%@}
%s:%i Hardware is not supported
-[NFAccessoryHardwareManager getRfSettings:]_block_invoke
-[NFAccessorySession synchronousRemoteObjectProxyWithErrorHandler:]
com.apple.NFAccessory.xpc
Line
-[NFAccessoryReaderSession(InternalTest) enableContinuousWave:withFrequencySweep:]_block_invoke
ndefContainerSize
-[NFAccessoryReaderSession startLpcdPolling:]_block_invoke
-[NFAccessoryReaderSession sendAccessoryProtocolCommand:outError:]_block_invoke
-[NFAccessoryHardwareManager startReaderSession:]_block_invoke
%s:%i Failed to get HW support : %{public}@
XPC Error
-[NFAccessorySession endSessionWithCompletion:]_block_invoke
ndefMessageSize
UID
B
v24@?0@\"NSArray\"8@\"NSError\"16
%s:%i HW not supported on this device
i
ndefAvailability
Generic A
Generic B
description
%s:%i Error: %{public}@
%s:%d
NFCIP
%s:%i %@
-[NFAccessorySession didStartSessionWithoutQueue:]
historicalBytes
-[NFAccessoryReaderSession sendAuthProtocolCommand:error:]
%s:%i Session ended before starting
-[NFAccessoryReaderSession stopPolling:]_block_invoke
v24@?0@\"NSError\"8@\"NSDictionary\"16
-[NFAccessoryHardwareManager getLastDetectedTags:]_block_invoke
-[NFAccessorySession didEndUnexpectedly]
Generic 3B
F
v20@?0B8@\"NSError\"12
-[NFAccessorySession dealloc]
-[NFAccessoryReaderSession checkPresence:]_block_invoke
updateHWSupport:Y
%{public}s:%i HW is not supported on this platform
%{public}s:%i started=%{public}@ 
%{public}s:%i Error = %{public}@
enableMultiTag:N
getLastDetectedTags:
%{public}s:%i HW not supported on this device
com.apple.nfcd.accessorySession.activeTimer
%s is still active after %lf seconds
%{public}s:%i %{public}@
connectTag:error:
%{public}s:%i Error: %{public}@
%{public}s:%i no proxy available
readNDEF:
sendAccessoryProtocolCommand:outError:
%{public}s:%i Failed to update HW support: %@
%{public}s:%i Hardware is not supported
%{public}s:%i XPC Failure: %{public}@
clearMultiTagState
%{public}s:%i Failed to get HW support : No XPC connection
%{public}s:%i Bad State
setTagDataRate:
%{public}s:%i %@
getRfSettings:
getInfo
enableLPCD:Y
enableLPCD:N
%{public}s:%i Failed to get HW support : %{public}@
%{public}s:%i endSession should have been called before dealloc
%{public}s:%i Session has terminated due to: %{public}@
startPollingForTechnology:error:
%{public}s:%i Unexpected connectionID (%lu vs %lu); dropping request
enableMultiTag:Y
pushSignedRF:
%{public}s:%i session ended
disconnectTag:
%{public}s:%i API has been deprecated!!!!
%{public}s:%i Connection has refreshed
getDieId:
getPowerCounteres:
endSessionWithCompletion:
%{public}s:%i 
%{public}s:%i Session ended before starting
stopPolling:
checkNdefSupport:andWrite:error:
transceive:error:
readTypeIdentifier:
%{public}s:%i Invalid connection, retry...
%{public}s:%i Retrying xpc connection - proxy error: %{public}@
triggerDelayedWake:
updateHWSupport:N
checkPresence:
startReaderSession:
getMultiTagState:
```
