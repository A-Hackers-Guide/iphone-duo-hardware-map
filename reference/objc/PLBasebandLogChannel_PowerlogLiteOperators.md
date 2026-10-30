# `PLBasebandLogChannel`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
^{__CFMessagePort=} remotePort;
^{__CFMessagePort=} localPort;
B cachingEnabled;
@"<PLBasebandLogChannelDelegate>" delegate;
```

## Properties

```
@property (T@"<PLBasebandLogChannelDelegate>",N,Vdelegate) delegate;
@property (TB,R,N) isValid;
@property (TB,N,VcachingEnabled) cachingEnabled;
```

## Instance methods

```
-[PLBasebandLogChannel close];
-[PLBasebandLogChannel init];
-[PLBasebandLogChannel flush];
-[PLBasebandLogChannel connectionInvalidated:];
-[PLBasebandLogChannel cachingEnabled];
-[PLBasebandLogChannel dealloc];
-[PLBasebandLogChannel invalidate];
-[PLBasebandLogChannel setDelegate:];
-[PLBasebandLogChannel isValid];
-[PLBasebandLogChannel delegate];
-[PLBasebandLogChannel setCachingEnabled:];
-[PLBasebandLogChannel commitHardwareLogs];
-[PLBasebandLogChannel enableLogCodes:andEvents:andExtraCode:];
-[PLBasebandLogChannel openWithConnection:];
-[PLBasebandLogChannel sendObjectOverRemotePort:];
-[PLBasebandLogChannel setChannelTimeout:];
-[PLBasebandLogChannel setHardwareLoggingLevel:withWindowSize:];
```
