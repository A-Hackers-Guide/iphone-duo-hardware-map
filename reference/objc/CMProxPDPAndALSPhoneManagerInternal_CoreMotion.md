# `CMProxPDPAndALSPhoneManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@? fPDPHandler;
@? fALSPhoneHandler;
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
B fStartedPDPUpdates;
B fStartedALSUpdates;
```

## Instance methods

```
-[CMProxPDPAndALSPhoneManagerInternal init];
-[CMProxPDPAndALSPhoneManagerInternal dealloc];
-[CMProxPDPAndALSPhoneManagerInternal _startALSPhoneUpdatesWithHandler:];
-[CMProxPDPAndALSPhoneManagerInternal _startPDPUpdatesWithHandler:];
```
