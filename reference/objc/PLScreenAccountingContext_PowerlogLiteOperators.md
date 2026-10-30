# `PLScreenAccountingContext`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _displayState;
Q _screenIndex;
@"NSDate" _lastScreenOnTime;
@"NSArray" _lastLayoutEntries;
@"NSMutableSet" _contextAppsOnScreen;
@"NSMutableSet" _contextPiPModeApps;
@"NSString" _screenStateEntryKey;
@"NSString" _displayEntryKey;
```

## Properties

```
@property (TQ,R,V_screenIndex) screenIndex;
@property (Ti,V_displayState) displayState;
@property (T@"NSDate",&,V_lastScreenOnTime) lastScreenOnTime;
@property (T@"NSArray",&,V_lastLayoutEntries) lastLayoutEntries;
@property (T@"NSMutableSet",&,V_contextAppsOnScreen) contextAppsOnScreen;
@property (T@"NSMutableSet",&,V_contextPiPModeApps) contextPiPModeApps;
@property (T@"NSString",R,V_screenStateEntryKey) screenStateEntryKey;
@property (T@"NSString",R,V_displayEntryKey) displayEntryKey;
```

## Instance methods

```
-[PLScreenAccountingContext setDisplayState:];
-[PLScreenAccountingContext displayState];
-[PLScreenAccountingContext displayEntryKey];
-[PLScreenAccountingContext contextAppsOnScreen];
-[PLScreenAccountingContext contextPiPModeApps];
-[PLScreenAccountingContext initWithScreenIndex:screenStateEntryKey:displayEntryKey:storage:];
-[PLScreenAccountingContext lastLayoutEntries];
-[PLScreenAccountingContext lastScreenOnTime];
-[PLScreenAccountingContext screenIndex];
-[PLScreenAccountingContext screenStateEntryKey];
-[PLScreenAccountingContext setContextAppsOnScreen:];
-[PLScreenAccountingContext setContextPiPModeApps:];
-[PLScreenAccountingContext setLastLayoutEntries:];
-[PLScreenAccountingContext setLastScreenOnTime:];
```
