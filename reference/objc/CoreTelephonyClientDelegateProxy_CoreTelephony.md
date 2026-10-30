# `CoreTelephonyClientDelegateProxy`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSProxy`
- Protocols: `CoreTelephonyClientDelegateProxyInterface`
- 2 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _userQueue;
@ _delegate;
```

## Properties

```
@property (T@,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CoreTelephonyClientDelegateProxy initWithQueue:];
-[CoreTelephonyClientDelegateProxy setDelegate:];
-[CoreTelephonyClientDelegateProxy delegate];
-[CoreTelephonyClientDelegateProxy methodSignatureForSelector:];
-[CoreTelephonyClientDelegateProxy forwardInvocation:];
```
