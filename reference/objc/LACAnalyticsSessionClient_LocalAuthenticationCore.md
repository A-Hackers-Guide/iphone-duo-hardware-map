# `LACAnalyticsSessionClient`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAnalyticsCollecting`
- 3 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
@"<LACContext>" _context;
@"<LACAnalyticsSessionXPC>" _session;
```

## Properties

```
@property (T@"<LACContext>",&,N) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACAnalyticsSessionClient initWithContext:];
-[LACAnalyticsSessionClient _connectionWithError:];
-[LACAnalyticsSessionClient setContext:];
-[LACAnalyticsSessionClient authenticationStartedForEvent:];
-[LACAnalyticsSessionClient context];
-[LACAnalyticsSessionClient finishSession];
-[LACAnalyticsSessionClient _bootstrapServiceWithError:];
-[LACAnalyticsSessionClient _callBlockOnSynchronousRemoteObjectProxy:];
-[LACAnalyticsSessionClient _connectionDidClose:];
-[LACAnalyticsSessionClient authenticationAction:failing:];
-[LACAnalyticsSessionClient authenticationAttemptFailedForEvent:];
-[LACAnalyticsSessionClient authenticationSuccessfulForEvent:];
-[LACAnalyticsSessionClient connectToExistingSession];
-[LACAnalyticsSessionClient startSessionForDialogID:bundleID:];
```
