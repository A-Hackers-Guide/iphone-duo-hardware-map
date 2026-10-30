# `SBBrightnessControl`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBrightnessRouteCoordinating`, `SBElasticHUDViewControllerDelegate`, `SBElasticBrightnessDataSource`
- 7 instance variables, 4 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"<SBHUDControlling>" _HUDController;
@"SBKeyboardBrightnessController" _keyboardBrightnessController;
@"SBDisplayBrightnessController" _displayBrightnessController;
@"<SBBrightnessRouteControlling>" _activeController;
B _controlCenterIsPresented;
B _brightnessIncrementKeyIsDown;
B _brightnessDecrementKeyIsDown;
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
+[SBBrightnessControl handlesKeyCommandsForRoute:];
```

## Instance methods

```
-[SBBrightnessControl _controlCenterWillPresent:];
-[SBBrightnessControl _controlCenterWillDismiss:];
-[SBBrightnessControl activeDataSource];
-[SBBrightnessControl setActiveController:];
-[SBBrightnessControl _HUDIsDisplayable];
-[SBBrightnessControl _HUDIsDisplayableWithReason:];
-[SBBrightnessControl _controllerForRoute:];
-[SBBrightnessControl _handleUpdateBrightnessIncrementKeyIsDown:decrementKeyIsDown:];
-[SBBrightnessControl _presentOrUpdateBrightnessHUDAsNecessaryForBrightnessLevel:];
-[SBBrightnessControl _resetIdleTimerForUserInteractionIfNecessary];
-[SBBrightnessControl _targetWindowScene];
-[SBBrightnessControl acquireBrightnessHUDHiddenAssertionForReason:];
-[SBBrightnessControl brightnessController:performCoordinatedBrightnessChangeForIncrementKeyDown:decrementKeyDown:];
-[SBBrightnessControl cancelBrightnessKeyPressEvents];
-[SBBrightnessControl elasticBrightnessViewControllerBrightnessRouteType:];
-[SBBrightnessControl elasticBrightnessViewControllerValueUpdatesDidEnd:];
-[SBBrightnessControl elasticBrightnessViewControllerValueUpdatesWillBegin:];
-[SBBrightnessControl elasticHUDViewControllerCanBePresented:withReason:];
-[SBBrightnessControl elasticHUDViewControllerRequestsDismissal:];
-[SBBrightnessControl elasticValueViewController:updateCurrentValue:];
-[SBBrightnessControl elasticValueViewControllerCurrentValue:];
-[SBBrightnessControl existingBrightnessHUDViewController];
-[SBBrightnessControl handleBrightnessKeyPressEvent:forRoute:];
-[SBBrightnessControl initWithHUDController:];
-[SBBrightnessControl presentedBrightnessHUDViewController];
-[SBBrightnessControl setBrightnessLevel:forRoute:];
```
