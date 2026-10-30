# `CTSubscriber`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientSubscriberDelegateInternal`
- 4 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _queue;
@"CoreTelephonyClient" _client;
@"<CTSubscriberDelegate>" _delegate;
@"CTServiceDescriptor" _descriptor;
```

## Properties

```
@property (T@"CTServiceDescriptor",&,N,V_descriptor) descriptor;
@property (T@"NSData",R,&,D,N) carrierToken;
@property (T@"NSString",R,N) identifier;
@property (TB,R,GisSIMInserted) SIMInserted;
@property (T@"<CTSubscriberDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CTSubscriber setDescriptor:];
-[CTSubscriber descriptor];
-[CTSubscriber identifier];
-[CTSubscriber init];
-[CTSubscriber initWithDescriptor:];
-[CTSubscriber setDelegate:];
-[CTSubscriber delegate];
-[CTSubscriber authTokenChanged:];
-[CTSubscriber _isValidGid:];
-[CTSubscriber _isValidMCCMNCString:max:min:];
-[CTSubscriber authenticate:completion:];
-[CTSubscriber authenticateWithInfo:handleResult:];
-[CTSubscriber carrierToken];
-[CTSubscriber initWithDescriptor:client:];
-[CTSubscriber isSIMInserted];
-[CTSubscriber refreshCarrierToken];
-[CTSubscriber simInserted];
-[CTSubscriber typeAllocationCode];
```
