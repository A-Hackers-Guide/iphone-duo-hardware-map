# `LARight`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LARightContextHandlerDelegate`
- 7 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"LAAccessKey" _accessKey;
@"LARightContextHandler" _contextHandler;
@"NSObject<OS_dispatch_queue>" _workQueue;
Q _instanceID;
q _state;
q _tag;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (Tq,N,V_tag) tag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LARight automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[LARight setState:];
-[LARight identifier];
-[LARight init];
-[LARight setTag:];
-[LARight dealloc];
-[LARight setContext:];
-[LARight tag];
-[LARight description];
-[LARight context];
-[LARight isEqual:];
-[LARight state];
-[LARight initWithRequirement:];
-[LARight accessKey];
-[LARight authorizeWithLocalizedReason:completion:];
-[LARight authorizeWithOptions:completion:];
-[LARight checkCanAuthorizeWithCompletion:];
-[LARight deauthorizeWithCompletion:];
-[LARight initWithAccessKey:];
-[LARight initWithIdentifier:accessKey:];
-[LARight rightContextDidBecomeInvalid];
```
