# `_UIContextMenuPanController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIContextMenuScrollObservationInteractionDelegate`
- 24 instance variables, 19 properties, 59 instance methods, 0 class methods

## Instance variables

```
Q _currentDetentIndex;
d _initialYTranslation;
d _defaultZPosition;
@"UIBezierPath" _menuScrubPath;
d _currentDistanceToMenuScrubPath;
{CGPoint="x"d"y"d} _initialLocationInsidePreview;
B _menuViewIsVisible;
B _touchEverEnteredMenu;
B _clientAllowsDismissal;
B _enabled;
B _platterPivotRotationEnabled;
@"UIViewSpringAnimationBehavior" _animationBehavior;
@"<_UIContextMenuPanControllerDelegate>" _delegate;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"NSArray" _detents;
Q _rubberbandingEdges;
@"NSArray" _accessoryViews;
@"UIView" _menuView;
@"UIView" _containerView;
@"UIView" _platterView;
@"_UIVelocityIntegrator" _velocityIntegrator;
{CGPoint="x"d"y"d} _originalPlatterCenter;
{CGPoint="x"d"y"d} _originalMenuCenter;
{?="attachment"Q"alignment"Q"attachmentOffset"d"alignmentOffset"d"gravity"q} _menuAnchor;
```

## Properties

```
@property (T@"UIView",W,N,V_containerView) containerView;
@property (T@"UIView",W,N,V_platterView) platterView;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (T@"_UIVelocityIntegrator",&,N,V_velocityIntegrator) velocityIntegrator;
@property (T@"UIViewSpringAnimationBehavior",R,N,V_animationBehavior) animationBehavior;
@property (T@"<_UIContextMenuPanControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_enabled) enabled;
@property (TB,N,V_platterPivotRotationEnabled) platterPivotRotationEnabled;
@property (T@"NSArray",&,N,V_detents) detents;
@property (T{CGPoint=dd},N,V_originalPlatterCenter) originalPlatterCenter;
@property (T{CGPoint=dd},N,V_originalMenuCenter) originalMenuCenter;
@property (T{?=QQddq},N,V_menuAnchor) menuAnchor;
@property (TQ,N,V_rubberbandingEdges) rubberbandingEdges;
@property (T@"NSArray",&,N,V_accessoryViews) accessoryViews;
@property (T@"UIView",W,N,V_menuView) menuView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuPanController platterView];
-[_UIContextMenuPanController panGestureRecognizer];
-[_UIContextMenuPanController setContainerView:];
-[_UIContextMenuPanController initWithContainerView:platterView:menuView:];
-[_UIContextMenuPanController setPanGestureRecognizer:];
-[_UIContextMenuPanController setPlatterView:];
-[_UIContextMenuPanController _updateForSignificantLayoutChange];
-[_UIContextMenuPanController gestureRecognizer:shouldReceiveTouch:];
-[_UIContextMenuPanController _currentPlatformMetrics];
-[_UIContextMenuPanController enabled];
-[_UIContextMenuPanController _initialPointInPlatterIsValid];
-[_UIContextMenuPanController gestureRecognizer:shouldReceiveEvent:];
-[_UIContextMenuPanController scrollObservationInteraction:didUpdateWithTranslation:location:ended:];
-[_UIContextMenuPanController _updateForGestureWithState:translation:location:allowsDragging:];
-[_UIContextMenuPanController _createAnimationBehaviorWithCriticalDamping:];
-[_UIContextMenuPanController setMenuView:];
-[_UIContextMenuPanController originalPlatterCenter];
-[_UIContextMenuPanController moveToDetentPosition:updateScrubPath:];
-[_UIContextMenuPanController scrollObservationInteraction:willBeginAtLocation:];
-[_UIContextMenuPanController _canSwipeDownToDismiss];
-[_UIContextMenuPanController _rangeOfMotion];
-[_UIContextMenuPanController _tearOffSpeedMultiplier];
-[_UIContextMenuPanController _animationsForActionsStyleWithLocation:ended:];
-[_UIContextMenuPanController _nearestDetentWithTranslation:];
-[_UIContextMenuPanController animationBehavior];
-[_UIContextMenuPanController menuAnchor];
-[_UIContextMenuPanController setAccessoryViews:];
-[_UIContextMenuPanController containerView];
-[_UIContextMenuPanController setDelegate:];
-[_UIContextMenuPanController setOriginalMenuCenter:];
-[_UIContextMenuPanController _userInterfaceIdiom];
-[_UIContextMenuPanController _animationsForAnyAttachedAccessoryViews];
-[_UIContextMenuPanController setEnabled:];
-[_UIContextMenuPanController _updateViewPositionsWithTranslation:location:ended:withVelocity:];
-[_UIContextMenuPanController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIContextMenuPanController accessoryViews];
-[_UIContextMenuPanController _rubberBandedTranslationForGestureTranslation:];
-[_UIContextMenuPanController originalMenuCenter];
-[_UIContextMenuPanController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIContextMenuPanController delegate];
-[_UIContextMenuPanController platterPivotRotationEnabled];
-[_UIContextMenuPanController detents];
-[_UIContextMenuPanController setPlatterPivotRotationEnabled:];
-[_UIContextMenuPanController _updatePlatterGestureDebugUIWithTranslation:location:invalidate:];
-[_UIContextMenuPanController rubberbandingEdges];
-[_UIContextMenuPanController velocityIntegrator];
-[_UIContextMenuPanController _currentPlatterVelocity];
-[_UIContextMenuPanController setMenuAnchor:];
-[_UIContextMenuPanController criticallyDampedAnimationBehavior];
-[_UIContextMenuPanController _handlePanGesture:];
-[_UIContextMenuPanController _animationsForPreviewPlusActionsStyleWithTranslation:location:];
-[_UIContextMenuPanController setOriginalPlatterCenter:];
-[_UIContextMenuPanController menuView];
-[_UIContextMenuPanController _dragTearOffThreshold];
-[_UIContextMenuPanController _canBeginDraggingWithTranslation:location:];
-[_UIContextMenuPanController setRubberbandingEdges:];
-[_UIContextMenuPanController setVelocityIntegrator:];
-[_UIContextMenuPanController setDetents:];
-[_UIContextMenuPanController _updateMenuScrubPathWithLocationIfNecessary:];
```
