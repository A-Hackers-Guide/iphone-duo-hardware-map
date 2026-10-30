# `ABMTapToRadar`

- Image: [`/usr/lib/libBasebandManagerDAL.dylib`](../userland/usr__lib__libBasebandManagerDAL.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
i fMode;
{queue="fObj"{object="fObj"^{dispatch_object_s}}} fQueue;
I fMaxUniqueSignatures;
I fMinTimeBetweenSameNotificationSec;
```

## Class methods

```
+[ABMTapToRadar sharedInstance];
```

## Instance methods

```
-[ABMTapToRadar init];
-[ABMTapToRadar setMode:];
-[ABMTapToRadar getMode];
-[ABMTapToRadar checkAudioTraces_sync];
-[ABMTapToRadar checkNotificationCriteria:::];
-[ABMTapToRadar checkTraces_sync:];
-[ABMTapToRadar findLogFiles_sync::];
-[ABMTapToRadar showNotification:::::];
-[ABMTapToRadar showUserNotification:dumpReason:];
```
