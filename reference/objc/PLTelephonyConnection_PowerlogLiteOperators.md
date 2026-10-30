# `PLTelephonyConnection`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
^{__CTServerConnection=} connection;
^{__CFMachPort=} ctServerPort;
^{__CFRunLoopSource=} ctServerSource;
@"PLAgent" _observerAgent;
```

## Properties

```
@property (T^{__CTServerConnection=},R,N) connection;
@property (T@"PLAgent",&,V_observerAgent) observerAgent;
```

## Class methods

```
+[PLTelephonyConnection sharedTelephonyConnection];
```

## Instance methods

```
-[PLTelephonyConnection init];
-[PLTelephonyConnection invalidate];
-[PLTelephonyConnection connection];
-[PLTelephonyConnection teardownConnection];
-[PLTelephonyConnection enableDiagLogging];
-[PLTelephonyConnection currentCallStatus];
-[PLTelephonyConnection deregisterForAllTelephonyNotifications];
-[PLTelephonyConnection getProperty:forTrace:];
-[PLTelephonyConnection getRAT:preferredRAT:campedRAT:];
-[PLTelephonyConnection getSignalStrength:asPercentage:withBars:];
-[PLTelephonyConnection humanReadableCallStatus:];
-[PLTelephonyConnection humanReadableRATName:];
-[PLTelephonyConnection observerAgent];
-[PLTelephonyConnection registerCallback:forTelephonyNotification:];
-[PLTelephonyConnection requestBasebandCoreDump:];
-[PLTelephonyConnection requestBasebandStateDump:];
-[PLTelephonyConnection setObserverAgent:];
```
