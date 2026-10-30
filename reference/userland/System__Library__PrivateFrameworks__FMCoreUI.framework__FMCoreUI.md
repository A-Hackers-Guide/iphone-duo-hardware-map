# `/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`

iOS 27.2 dyld shared cache image. Version `196.31.6.16.2`. **[DSC]**

## Linked libraries (14)

- `/System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/Frameworks/Contacts.framework/Contacts`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`
- `/System/Library/PrivateFrameworks/FMCore.framework/FMCore`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/Frameworks/MapKit.framework/MapKit`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials`
- `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

## Objective-C: 37 classes, 7 protocols, 615 methods, 151 properties

### Class pages

Every class and protocol, with its methods: [`FMAccuracyOverlay`](../objc/FMAccuracyOverlay_FMCoreUI.md), [`FMAnnotation`](../objc/FMAnnotation_FMCoreUI.protocol.md), [`FMAnnotationView`](../objc/FMAnnotationView_FMCoreUI.md), [`FMAppShortcutManager`](../objc/FMAppShortcutManager_FMCoreUI.md), [`FMAttributedStringRenderer`](../objc/FMAttributedStringRenderer_FMCoreUI.md), [`FMAttributedStringRendererOptions`](../objc/FMAttributedStringRendererOptions_FMCoreUI.md), [`FMBlurView`](../objc/FMBlurView_FMCoreUI.md), [`FMBorderedButton`](../objc/FMBorderedButton_FMCoreUI.md), [`FMBorderedField`](../objc/FMBorderedField_FMCoreUI.md), [`FMBorderedView`](../objc/FMBorderedView_FMCoreUI.md), [`FMBottomPaneSegue`](../objc/FMBottomPaneSegue_FMCoreUI.md), [`FMDistanceBadge`](../objc/FMDistanceBadge_FMCoreUI.md), [`FMFixedSizeView`](../objc/FMFixedSizeView_FMCoreUI.md), [`FMHairlineConstraint`](../objc/FMHairlineConstraint_FMCoreUI.md), [`FMHorizontalRule`](../objc/FMHorizontalRule_FMCoreUI.md), [`FMLeftPaneSegue`](../objc/FMLeftPaneSegue_FMCoreUI.md), [`FMMapAnnotationGestureRecognizer`](../objc/FMMapAnnotationGestureRecognizer_FMCoreUI.md), [`FMMapAnnotationGestureRecognizerDelegate`](../objc/FMMapAnnotationGestureRecognizerDelegate_FMCoreUI.protocol.md), [`FMMapGestureRecognizer`](../objc/FMMapGestureRecognizer_FMCoreUI.md), [`FMMapGestureRecognizerDelegate`](../objc/FMMapGestureRecognizerDelegate_FMCoreUI.protocol.md), [`FMMapView`](../objc/FMMapView_FMCoreUI.md), [`FMObservingCell`](../objc/FMObservingCell_FMCoreUI.md), [`FMPaneSegue`](../objc/FMPaneSegue_FMCoreUI.md), [`FMRightPaneSegue`](../objc/FMRightPaneSegue_FMCoreUI.md), [`FMRule`](../objc/FMRule_FMCoreUI.md), [`FMSlidingPaneViewController`](../objc/FMSlidingPaneViewController_FMCoreUI.md), [`FMTitleView`](../objc/FMTitleView_FMCoreUI.md), [`FMTitleViewCenteringNavigationBar`](../objc/FMTitleViewCenteringNavigationBar_FMCoreUI.md), [`FMTopPaneSegue`](../objc/FMTopPaneSegue_FMCoreUI.md), [`FMUserLocationView`](../objc/FMUserLocationView_FMCoreUI.md), [`FMVerticalRule`](../objc/FMVerticalRule_FMCoreUI.md), [`FMViewController`](../objc/FMViewController_FMCoreUI.md), [`FM_Workaround_30408319_Button`](../objc/FM_Workaround_30408319_Button_FMCoreUI.md), [`ISPaneFrameView`](../objc/ISPaneFrameView_FMCoreUI.md), [`MKMapViewDelegate`](../objc/MKMapViewDelegate_FMCoreUI.protocol.md), [`MKUserTrackingView`](../objc/MKUserTrackingView_FMCoreUI.protocol.md), [`NSObject`](../objc/NSObject_FMCoreUI.protocol.md), [`SlidingPaneViewState`](../objc/SlidingPaneViewState_FMCoreUI.md), [`UIGestureRecognizerDelegate`](../objc/UIGestureRecognizerDelegate_FMCoreUI.protocol.md)

### Classes

`FMAccuracyOverlay`, `FMAnnotationView`, `FMAppShortcutManager`, `FMAttributedStringRenderer`, `FMAttributedStringRendererOptions`, `FMBlurView`, `FMBorderedButton`, `FMBorderedField`, `FMBorderedView`, `FMBottomPaneSegue`, `FMDistanceBadge`, `FMFixedSizeView`, `FMHairlineConstraint`, `FMHorizontalRule`, `FMLeftPaneSegue`, `FMMapAnnotationGestureRecognizer`, `FMMapGestureRecognizer`, `FMMapView`, `FMObservingCell`, `FMPaneSegue`, `FMRightPaneSegue`, `FMRule`, `FMSlidingPaneViewController`, `FMTitleView`, `FMTitleViewCenteringNavigationBar`, `FMTopPaneSegue`, `FMUserLocationView`, `FMVerticalRule`, `FMViewController`, `FM_Workaround_30408319_Button`, `ISPaneFrameView`, `SlidingPaneViewState`, `UIColor`, `UIImage`, `UIScrollView`, `UIView`, `UIViewController`

### Protocols

`FMAnnotation`, `FMMapAnnotationGestureRecognizerDelegate`, `FMMapGestureRecognizerDelegate`, `MKMapViewDelegate`, `MKUserTrackingView`, `NSObject`, `UIGestureRecognizerDelegate`

### Properties

```
@property (T@"FMAccuracyOverlay",&,N) overlay;
@property (Td,N) horizontalAccuracy;
@property (T{CLLocationCoordinate2D=dd},N) coordinate;
@property (Td,N) distanceFromUser;
@property (TB,N) isBorderEnabled;
@property (T@"UIColor",&,N) tintColor;
@property (T@"UIImage",&,N) largeAnnotationIcon;
@property (T@"UIImage",&,N) smallAnnotationIcon;
@property (T@"UIImage",&,N) largeOverlayIcon;
@property (T@"UIImage",&,N) smallOverlayIcon;
@property (T@"NSString",?,R,C,N) title;
@property (T@"NSString",?,R,C,N) subtitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<MKAnnotation>",W,N,V_parentAnnotation) parentAnnotation;
@property (Td,N,V_horizontalAccuracy) horizontalAccuracy;
@property (T@"CAShapeLayer",&,N,V_smallRingLayer) smallRingLayer;
@property (T@"CAShapeLayer",&,N,V_largeRingLayer) largeRingLayer;
@property (T@"CALayer",&,N,V_smallCircleLayer) smallCircleLayer;
@property (T@"CALayer",&,N,V_largeCircleLayer) largeCircleLayer;
@property (T@"CALayer",&,N,V_locationOuterLayer) locationOuterLayer;
@property (T@"CALayer",&,N,V_locationInnerLayer) locationInnerLayer;
@property (T@"CALayer",&,N,V_smallPersonImageLayer) smallPersonImageLayer;
@property (T@"CALayer",&,N,V_largePersonImageLayer) largePersonImageLayer;
@property (TB,N,V_isShowingLargeSelectedAnnotation) isShowingLargeSelectedAnnotation;
@property (TB,N,V_hasPhotoImage) hasPhotoImage;
@property (T@"<FMAnnotation><MKAnnotation>",&,D,N) annotation;
@property (TB,N,V_shouldPreventLargeAnnotationState) shouldPreventLargeAnnotationState;
@property (TB,N,V_isDelayed) isDelayed;
@property (TB,R) hasShortcutItems;
@property (T@"FMAttributedStringRendererOptions",R,N,V_options) options;
@property (Tq,R,N,V_lineBreakMode) lineBreakMode;
@property (Td,R,N,V_lineFragmentPadding) lineFragmentPadding;
@property (TQ,R,N,V_maximumNumberOfLines) maximumNumberOfLines;
@property (Td,R,N,V_hyphenationFactor) hyphenationFactor;
@property (T@"NSArray",R,C,N,V_exclusionPaths) exclusionPaths;
@property (TB,N,V_autosizesToFitSuperview) autosizesToFitSuperview;
@property (TB,N,V_hairlineBorder) hairlineBorder;
@property (Td,N) borderWidth;
@property (Td,N) cornerRadius;
@property (T@"UIColor",&,N,V_borderColor) borderColor;
@property (TB,N,V_isConfigured) isConfigured;
@property (T@"FMHorizontalRule",&,N,V_topRule) topRule;
@property (T@"FMHorizontalRule",&,N,V_bottomRule) bottomRule;
@property (T@"UIColor",&,N,V_borderColor) borderColor;
@property (TB,N,V_hairlineBorder) hairlineBorder;
@property (Td,N) borderWidth;
@property (Td,N) cornerRadius;
@property (T@"UIColor",&,N) borderColor;
@property (T{UIEdgeInsets=dddd},N,V_insets) insets;
@property (T@"UIColor",&,N,V_badgeColor) badgeColor;
@property (T{CGSize=dd},N,V_fixedIntrinsicSize) fixedIntrinsicSize;
@property (Td,N,V_pixelHeight) pixelHeight;
@property (T@"<FMMapAnnotationGestureRecognizerDelegate>",N,V_touchDelegate) touchDelegate;
@property (T{CGPoint=dd},N,V_initialTouchLocation) initialTouchLocation;
@property (T@"UITouch",&,N,V_previousTouch) previousTouch;
@property (T{CGPoint=dd},N,V_lastTouchPoint) lastTouchPoint;
@property (Td,N,V_swipeThreshold) swipeThreshold;
@property (Td,N,V_velocity) velocity;
@property (TB,N,V_isTrackingTouches) isTrackingTouches;
@property (TB,N,V_isSwipingFromTheEdge) isSwipingFromTheEdge;
@property (TB,N,V_isSwipingGestureEnded) isSwipingGestureEnded;
@property (TB,N,V_isRTLOrientation) isRTLOrientation;
@property (T@"NSMutableArray",&,N,V_otherGestures) otherGestures;
@property (T@"NSTimer",&,N,V_doubleTapTimer) doubleTapTimer;
@property (T@"<FMMapGestureRecognizerDelegate>",W,N,V_touchDelegate) touchDelegate;
@property (Ti,N,V_touchRadius) touchRadius;
@property (TB,N,V_isSwipeEnabled) isSwipeEnabled;
@property (T@"FMMapGestureRecognizer",&,N,V_mapGesture) mapGesture;
@property (T{?={?=dd}{?=dd}},N,V_lastVisibleMapRect) lastVisibleMapRect;
@property (T@"<FMAnnotation><MKAnnotation>",W,N,V_lastSelectedAnnotationBeforeTracking) lastSelectedAnnotationBeforeTracking;
@property (T@"MKMapCamera",&,N,V_cameraBefore3DRendering) cameraBefore3DRendering;
@property (T@"NSTimer",&,N,V_layoutTimer) layoutTimer;
@property (Td,N,V_maxZoomLevel) maxZoomLevel;
@property (T{UIEdgeInsets=dddd},N,V_lastVisibleInsets) lastVisibleInsets;
@property (TB,N,V_isUserLocationUpdated) isUserLocationUpdated;
@property (TB,N,V_canChangeUserTrackingMode) canChangeUserTrackingMode;
@property (TB,N,V_isGoingBackToAllAnnotation) isGoingBackToAllAnnotation;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (TB,N,V_isSwitchingTrackingMode) isSwitchingTrackingMode;
@property (TB,N,V_shouldDisplayOverlay) shouldDisplayOverlay;
@property (TB,N,V_canSelectUserAnnotation) canSelectUserAnnotation;
@property (T@"NSTimer",&,N,V_userSelectionTimer) userSelectionTimer;
@property (T@"FMAnnotationView",&,N,V_potentiallySelectedAnnotationView) potentiallySelectedAnnotationView;
@property (T@"FMAnnotationView",&,N,V_selectedAnnotationView) selectedAnnotationView;
@property (T@"MKUserLocationView",W,N,V_userLocationView) userLocationView;
@property (T@"MKUserLocation",&,N,V_userLocation) userLocation;
@property (T@"<FMAnnotation><MKAnnotation>",W,N,V_currentDeviceAnnotation) currentDeviceAnnotation;
@property (T@"<MKAnnotation>",W,N,V_otherSelectedAnnotation) otherSelectedAnnotation;
@property (Tq,N,V_currentSelectedState) currentSelectedState;
@property (T@"NSMutableArray",&,N,V_accuracyOverlays) accuracyOverlays;
@property (TB,N,V_isFingerOnMap) isFingerOnMap;
@property (TB,N,V_isFingerOnAnnotation) isFingerOnAnnotation;
@property (TB,N,V_isMapMoved) isMapMoved;
@property (T@"<FMMapViewDelegate>",W,N,V_delegate) delegate;
@property (T@"MKMapView",R,N,V_mapView) mapView;
@property (T@"_MKUserTrackingButton",&,N,V_userTrackingButton) userTrackingButton;
@property (T@"UIColor",&,N,V_userLocationTintColor) userLocationTintColor;
@property (Tq,N,V_currentTrackingMode) currentTrackingMode;
@property (Tq,N,V_doubleSelectionMode) doubleSelectionMode;
@property (Tq,N,V_renderingMode) renderingMode;
@property (TB,N,V_isAllAnnotationsShown) isAllAnnotationsShown;
@property (TB,N,V_isMapPositioningDisabled) isMapPositioningDisabled;
@property (TB,N,V_isSwipeGestureEnabled) isSwipeGestureEnabled;
@property (TB,N,V_isMapAnimating) isMapAnimating;
@property (TB,N,V_isUserSwiping) isUserSwiping;
@property (TB,N,V_isNearbyModeDisabled) isNearbyModeDisabled;
@property (TB,N,V_showUserLocationCallout) showUserLocationCallout;
@property (TB,N,V_isPreventingMapUpdates) isPreventingMapUpdates;
@property (T@"<FMAnnotation><MKAnnotation>",W,N,V_selectedAnnotation) selectedAnnotation;
@property (TB,N,V_isPreviewing) isPreviewing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",&,N,V_kvoObservationTokens) kvoObservationTokens;
@property (T@"NSMutableSet",&,N,V_notificationTokens) notificationTokens;
@property (T@,W,N,V_representedObject) representedObject;
@property (TB,N,V_disableAnimation) disableAnimation;
@property (TB,N,V_leading) leading;
@property (T@"UIColor",&,N,V_color) color;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (T@"SlidingPaneViewState",&,N,V_paneState) paneState;
@property (TB,N,V_didHideToolbar) didHideToolbar;
@property (T@"NSMutableArray",&,N,V_actionFutures) actionFutures;
@property (T@"FMFuture",R,N) currentFuture;
@property (T@"<FMSlidingPaneViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIViewController",R,N) paneViewController;
@property (T@"UIView",R,N) paneView;
@property (T{UIEdgeInsets=dddd},N,V_paneInsets) paneInsets;
@property (T{UIEdgeInsets=dddd},N,V_paneContentInsets) paneContentInsets;
@property (Td,N,V_animationDuration) animationDuration;
@property (Td,N,V_animationSpringDamping) animationSpringDamping;
@property (Td,N,V_animationInitialVelocity) animationInitialVelocity;
@property (TQ,N,V_animationOptions) animationOptions;
@property (T@"UIVisualEffect",&,N,V_paneVisualEffect) paneVisualEffect;
@property (TB,R,N,GisPaneShowing) paneShowing;
@property (T@"NSMutableDictionary",&,N,V_kvoObservationTokens) kvoObservationTokens;
@property (T@"NSMutableSet",&,N,V_notificationTokens) notificationTokens;
@property (T@"NSString",R,C) controllerNibName;
@property (T@"NSLayoutConstraint",&,N,V_fm_workaround_height_constraint) fm_workaround_height_constraint;
@property (T@"FMSlidingPaneViewController",W,N,V_owningViewController) owningViewController;
@property (T@"UIViewController",&,N,V_paneViewController) paneViewController;
@property (T@"ISPaneFrameView",&,N,V_paneView) paneView;
@property (T@"UIVisualEffectView",&,N,V_visualEffectView) visualEffectView;
@property (T@"NSLayoutConstraint",&,N,V_paneVerticalPositionConstraint) paneVerticalPositionConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paneHorizontalPositionConstraint) paneHorizontalPositionConstraint;
@property (TB,N,V_shouldNotifyOfPaneSizeChanges) shouldNotifyOfPaneSizeChanges;
@property (TQ,N,V_edge) edge;
```

## Strings (137)

```
V:|-0-[mapView]-0-|
UIImage+Compositing.m
mapView
preferredHeight
Must be subclassed
borderColor
v8@?0
x
left
FMSlidingPaneViewController.m
width > 0.0
H:[self(width)]
_iPad
FMMKUserAnnotationReuseIdentifier
y
top
FIXME: Test this code path.  As of Whitetail MapKit was never calling this method and it was just added for protocol conformance.
!
FMTitleView.m
V:|[self]|
H:|[self]|
FMMapViewRepositionNotification
paneView
1\"
constraintToFillSuperview.V
ViewController
nib
<%@: %p> [%@] %.6f/%6f @ %f
_
right
paneVerticalPositionConstant
newPaneState != nil
annotation_location_outer
view
constraintToFillSuperview.H
v24@?0@\"NSNull\"8@\"NSError\"16
FMRoundedRectBackgroundColorKey
FMAnnotationView.m
d16@?0d8
com.apple.icloud.FMCoreUI
H:|-left-[paneView]-right-|
self
ISCommonUI+PreviousBorderColor
ISCommonUI+PreviousBorderWidth
annotation_location_inner
V:|[view]|
_iPhone
vc
v12@?0B8
layoutManager.textContainers.count == 1
FMColorInvertFilter
FMViewController.m
FMSlidingPaneViewController
q24@?0@\"<FMAnnotation><MKAnnotation>\"8@\"<FMAnnotation><MKAnnotation>\"16
depthSortAnnotations
FMMapView.synchronize
contentView
fm_workaround_height_constraint
[navbar isKindOfClass:[UINavigationBar class]]
FMMapViewLastVisibleRect
height
bottom
H:|-left-[contentView]-right-|
paneState != nil
[[inToken class] respondsToSelector:@selector(isAnObserver:)]
V:[self(height)]
Invalid parameter not satisfying: %@
FMAnnotationViewReuseIdentifier
FMObservingCell.m
annotation_circle_large
v16@?0@\"UIGraphicsImageRendererContext\"8
No instance of FMSlidingPaneViewController in controller hierarchy of %@
FMMapViewLastVisibleInsets
FMMapView.m
layoutManager.textStorage != nil
Don't call this!
B32@?0@\"CAFilter\"8Q16^B24
H:|[view]|
V:|-top-[paneView]-bottom-|
V:|-top-[contentView]-bottom-|
FMAttributedStringRenderer.m
Cannot derive nib name from class [%@]
FMShortcutItemIdentifierKey
retValue != nil
width
H:|-0-[mapView]-0-|
preferredWidth
paneHorizontalPositionConstraint
oldPaneState != nil
FMRoundedRectBorderColorKey
FMRoundedRectBorderWidthKey
A
ISCommonUI+DebugHighlight
ISCommonUI+PreviousBackgroundColor
annotation_circle_small
transform
Calling present completion block
Attempted to add nil KVO token!
FMAnnotationView: _transitionToNewSize delayed?: %d
Unable to remove KVO tokenSet [%@] because observedObject is nil!
Item is - %@
FMMapView: delegate insets %@ currentState: %ld
FMMapView: setting 3D camera %@
Bad systemLayoutSize: %@ from constraints: %@
Error archiving FMMapViewLastVisibleRect: %@
Deferring presenting until previous action is complete
_dismissPaneState: %@ animated: %d completion:
Calling willDismissPane: %@ animated: %d
Setting initial shortcut items.
Expected overlay to be FMAccuracyOverlay!
presentPaneViewController: %@ fromEdge:%ld animated:%d completed:
presentPaneViewController: %@ fromEdge:%ld withPercent:%f completion:
Dismissing pane while previous pane is still presenting: %@
_presentPaneState: %@ animated:%d interactive:%d completion:
addChildViewController: %@
No customRendererForOverlay!
Calling willPresentPane: %@ inRect: %@ animated:%d
All shortcut items are cleared
FMMapView: animateMapToPosition insets %@ safeArea: %f
FMMapView: viewSize: %@ bounds: %@ safeInsets: %@
Calling didPresentPane: %@ inRect: %@ animated:%d
Calling willDismissPane: %@ animated:%d
Calling paneSizeChanged: %@ forViewController: %@
Un-normalized size: %@
Calling dismiss completionBlock
Deferring dismissing until previous action is complete
FMAnnotationView: setSelected: %d, animated: %d delay: %f
FMAnnotationView: _selectionWasUpdated isShowingLargeAnotation: %d, isSelected: %d
Leaked KVO Observer: %@
New shortcut item passed - %@
animateMapToPosition isMapAnimating(%d) layoutTimer(%d) isPreventingMapUpdates(%d) duration(%f)
Error archiving FMMapViewLastVisibleInsets: %@
Calling didDismissPane: %@ animated:%d
FMAnnotationView: setSelected: %d, animated: %d
Unknown edge: %lu
dismissPaneViewControllerAnimated:%d completion:
_removeChildViewControllerForState: %@
```
