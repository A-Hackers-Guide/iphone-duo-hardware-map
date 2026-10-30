# `AUParameterTree`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUParameterGroup`
- Protocols: `NSSecureCoding`
- 10 instance variables, 9 properties, 26 instance methods, 6 class methods

## Instance variables

```
{shared_ptr<AUObserverController>="__ptr_"^{AUObserverController}"__cntrl_"^{__shared_weak_count}} _observerController;
i __autoCreatedForV2AU;
i _numRecorders;
@"NSObject<OS_dispatch_queue>" _observationQueue;
@"NSObject<OS_dispatch_queue>" _valueAccessQueue;
@"AUAudioUnit_XH" __auXH;
^{AURemoteParameterObserver=} _remoteObserverToken;
^{AURemoteParameterObserver=} _remoteRecorderToken;
@"NSXPCConnection" _remoteParameterSynchronizerXPCConnection;
{vector<AddressToParameter, std::allocator<AddressToParameter>>="__begin_"^{AddressToParameter}"__end_"^{AddressToParameter}""{?="__cap_"^{AddressToParameter}}} _addrToParamIndex;
```

## Properties

```
@property (T{vector<AddressToParameter, std::allocator<AddressToParameter>>=^{AddressToParameter}^{AddressToParameter}{?=^{AddressToParameter}}},N,V_addrToParamIndex) addrToParamIndex;
@property (Ti,N,V__autoCreatedForV2AU) _autoCreatedForV2AU;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_observationQueue) observationQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_valueAccessQueue) valueAccessQueue;
@property (T@"AUAudioUnit_XH",W,N,V__auXH) _auXH;
@property (Ti,N,V_numRecorders) numRecorders;
@property (T^{AURemoteParameterObserver=},N,V_remoteObserverToken) remoteObserverToken;
@property (T^{AURemoteParameterObserver=},N,V_remoteRecorderToken) remoteRecorderToken;
@property (T@"NSXPCConnection",W,N,V_remoteParameterSynchronizerXPCConnection) remoteParameterSynchronizerXPCConnection;
```

## Class methods

```
+[AUParameterTree supportsSecureCoding];
+[AUParameterTree createGroupFromTemplate:identifier:name:addressOffset:];
+[AUParameterTree createGroupTemplate:];
+[AUParameterTree createGroupWithIdentifier:name:children:];
+[AUParameterTree createParameterWithIdentifier:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:];
+[AUParameterTree createTreeWithChildren:];
```

## Instance methods

```
-[AUParameterTree _init2];
-[AUParameterTree _checkInitTreeObservation];
-[AUParameterTree parameterWithID:scope:element:];
-[AUParameterTree remoteRecorderToken];
-[AUParameterTree dealloc];
-[AUParameterTree remoteObserverToken];
-[AUParameterTree setRemoteObserverToken:];
-[AUParameterTree set_auXH:];
-[AUParameterTree numRecorders];
-[AUParameterTree setNumRecorders:];
-[AUParameterTree setRemoteParameterSynchronizerXPCConnection:];
-[AUParameterTree setRemoteRecorderToken:];
-[AUParameterTree observationQueue];
-[AUParameterTree encodeWithCoder:];
-[AUParameterTree _autoCreatedForV2AU];
-[AUParameterTree set_autoCreatedForV2AU:];
-[AUParameterTree initWithCoder:];
-[AUParameterTree setAddrToParamIndex:];
-[AUParameterTree parameterWithAddress:];
-[AUParameterTree _auXH];
-[AUParameterTree addrToParamIndex];
-[AUParameterTree remoteSyncParameter:value:extOriginator:hostTime:eventType:];
-[AUParameterTree remoteParameterSynchronizerXPCConnection];
-[AUParameterTree valueAccessQueue];
-[AUParameterTree observerController];
-[AUParameterTree initWithChildren:];
```
