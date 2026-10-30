# `SBScheduledAlarmObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSoundObserver`
- 1 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"MTAlarmManager" _alarmManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBScheduledAlarmObserver sharedInstance];
```

## Instance methods

```
-[SBScheduledAlarmObserver init];
-[SBScheduledAlarmObserver alert:didBeginPlayingWithEvent:];
-[SBScheduledAlarmObserver _alarmFiringChanged:];
-[SBScheduledAlarmObserver _nextAlarmChanged:];
-[SBScheduledAlarmObserver _updateAlarmFiringChangedWithAlarm:];
-[SBScheduledAlarmObserver _updateAlarmStatusBarItem];
-[SBScheduledAlarmObserver soundDidBeginPlaying:];
-[SBScheduledAlarmObserver soundDidFinishPlaying:];
```
