# `IMUDeviceMotionDelegateObserverImpl`

- Image: [`/usr/lib/libBasebandManagerICE.dylib`](../userland/usr__lib__libBasebandManagerICE.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"CMMotionManager" fMotionManager;
@"NSOperationQueue" fQueue;
{function<void (IMUDeviceMotionDelegate::IMUMotionInfo)>="__f_"{__value_func<void (IMUDeviceMotionDelegate::IMUMotionInfo)>="__buf_"(type="__data"[24C])"__f_"^v}} fCallback;
f fThresholdPortraitUpright;
f fThresholdPortraitUpsideDown;
f fThresholdLandscapeLeft;
f fThresholdLandscapeRight;
f fPitchMinThreshold;
f fPitchMaxThreshold;
f fRollMinThreshold;
f fRollMaxThreshold;
```

## Instance methods

```
-[IMUDeviceMotionDelegateObserverImpl stop];
-[IMUDeviceMotionDelegateObserverImpl dealloc];
-[IMUDeviceMotionDelegateObserverImpl start];
-[IMUDeviceMotionDelegateObserverImpl registerHandler:];
-[IMUDeviceMotionDelegateObserverImpl init:];
-[IMUDeviceMotionDelegateObserverImpl setThresholdPortraitUpsideDown:];
-[IMUDeviceMotionDelegateObserverImpl computeIMUSensingAnalytics:pitchDeg:rollDeg:gz:];
-[IMUDeviceMotionDelegateObserverImpl getAngleDelta:g2:];
-[IMUDeviceMotionDelegateObserverImpl getPitchMaxThreshold];
-[IMUDeviceMotionDelegateObserverImpl getPitchMinThreshold];
-[IMUDeviceMotionDelegateObserverImpl getRollMaxThreshold];
-[IMUDeviceMotionDelegateObserverImpl getRollMinThreshold];
-[IMUDeviceMotionDelegateObserverImpl getThresholdLandscapeLeft];
-[IMUDeviceMotionDelegateObserverImpl getThresholdLandscapeRight];
-[IMUDeviceMotionDelegateObserverImpl getThresholdPortraitUpright];
-[IMUDeviceMotionDelegateObserverImpl getThresholdPortraitUpsideDown];
-[IMUDeviceMotionDelegateObserverImpl setPitchMaxThreshold:];
-[IMUDeviceMotionDelegateObserverImpl setPitchMinThreshold:];
-[IMUDeviceMotionDelegateObserverImpl setRollMaxThreshold:];
-[IMUDeviceMotionDelegateObserverImpl setRollMinThreshold:];
-[IMUDeviceMotionDelegateObserverImpl setThresholdLandscapeLeft:];
-[IMUDeviceMotionDelegateObserverImpl setThresholdLandscapeRight:];
-[IMUDeviceMotionDelegateObserverImpl setThresholdPortraitUpright:];
```
