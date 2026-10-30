# `SBAnalyticsContextProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAnalyticsBackendEventContextProviding`
- 2 instance variables, 5 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBSAnalyticsState" _eventPayload;
@"SBFAnalyticsBackend" _backend;
```

## Properties

```
@property (T@"SBSAnalyticsState",R,N) eventPayload;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAnalyticsContextProvider description];
-[SBAnalyticsContextProvider eventPayload];
-[SBAnalyticsContextProvider initWithEventPayload:backend:];
-[SBAnalyticsContextProvider stateForQueryName:completion:];
```
