# `StateABDelegateObserverImpl`

- Image: [`/usr/lib/libBasebandManagerICE.dylib`](../userland/usr__lib__libBasebandManagerICE.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"CMAngleManager" fAngleManager;
@? fCMAngleHandler;
@"NSOperationQueue" fQueue;
{function<void (StateABDelegate::StateABInfo)>="__f_"{__value_func<void (StateABDelegate::StateABInfo)>="__buf_"(type="__data"[24C])"__f_"^v}} fCallback;
B fAngleIsAvailable;
f fThresholdStateBForTuner;
f fOsirisState1ThresholdMin;
f fOsirisState1ThresholdMax;
f fOsirisState2ThresholdMin;
f fOsirisState2ThresholdMax;
f fOsirisState3ThresholdMin;
f fOsirisState3ThresholdMax;
```

## Instance methods

```
-[StateABDelegateObserverImpl registerCallback:];
-[StateABDelegateObserverImpl stop];
-[StateABDelegateObserverImpl dealloc];
-[StateABDelegateObserverImpl start];
-[StateABDelegateObserverImpl init:];
-[StateABDelegateObserverImpl getOsirisState1MaxThreshold];
-[StateABDelegateObserverImpl getOsirisState1MinThreshold];
-[StateABDelegateObserverImpl getOsirisState2MaxThreshold];
-[StateABDelegateObserverImpl getOsirisState2MinThreshold];
-[StateABDelegateObserverImpl getOsirisState3MaxThreshold];
-[StateABDelegateObserverImpl getOsirisState3MinThreshold];
-[StateABDelegateObserverImpl getTunerThreshold];
-[StateABDelegateObserverImpl setOsirisState1MaxThreshold:];
-[StateABDelegateObserverImpl setOsirisState1MinThreshold:];
-[StateABDelegateObserverImpl setOsirisState2MaxThreshold:];
-[StateABDelegateObserverImpl setOsirisState2MinThreshold:];
-[StateABDelegateObserverImpl setOsirisState3MaxThreshold:];
-[StateABDelegateObserverImpl setOsirisState3MinThreshold:];
-[StateABDelegateObserverImpl setTunerThreshold:];
```
