# `SBCaptureApplicationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
d _launchMonitorDurationInSeconds;
d _launchAssertionTimeOutDurationInSeconds;
```

## Properties

```
@property (Td,N,V_launchMonitorDurationInSeconds) launchMonitorDurationInSeconds;
@property (Td,N,V_launchAssertionTimeOutDurationInSeconds) launchAssertionTimeOutDurationInSeconds;
```

## Class methods

```
+[SBCaptureApplicationSettings settingsControllerModule];
```

## Instance methods

```
-[SBCaptureApplicationSettings setDefaultValues];
-[SBCaptureApplicationSettings launchAssertionTimeOutDurationInSeconds];
-[SBCaptureApplicationSettings launchMonitorDurationInSeconds];
-[SBCaptureApplicationSettings setLaunchAssertionTimeOutDurationInSeconds:];
-[SBCaptureApplicationSettings setLaunchMonitorDurationInSeconds:];
```
