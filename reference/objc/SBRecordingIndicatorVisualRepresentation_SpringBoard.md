# `SBRecordingIndicatorVisualRepresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRecordingIndicatorConfiguring`, `SAUIElementViewCustomBlurAccepting`
- 6 instance variables, 12 properties, 13 instance methods, 1 class methods

## Instance variables

```
Q _viewType;
@"CALayer<SBRecordingIndicatorLayering>" _highLevelLayer;
@"SBRecordingIndicatorView" _highLevelView;
@"SBRecordingIndicatorView" _contentView;
@"SBRecordingIndicatorContainerView" _containerView;
@"SBRecordingIndicatorPortalView" _portalView;
```

## Properties

```
@property (TQ,N) indicatorType;
@property (TQ,R,N,V_viewType) viewType;
@property (T@"CALayer<SBRecordingIndicatorLayering>",R,N,V_highLevelLayer) highLevelLayer;
@property (T@"SBRecordingIndicatorView",R,N,V_highLevelView) highLevelView;
@property (T@"SBRecordingIndicatorView",R,N,V_contentView) contentView;
@property (T@"SBRecordingIndicatorContainerView",R,N,V_containerView) containerView;
@property (T@"SBRecordingIndicatorPortalView",R,N,V_portalView) portalView;
@property (Td,N) blurRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBRecordingIndicatorVisualRepresentation indicatorFrameForWindowScene:style:];
```

## Instance methods

```
-[SBRecordingIndicatorVisualRepresentation portalView];
-[SBRecordingIndicatorVisualRepresentation setIndicatorType:];
-[SBRecordingIndicatorVisualRepresentation containerView];
-[SBRecordingIndicatorVisualRepresentation blurRadius];
-[SBRecordingIndicatorVisualRepresentation contentView];
-[SBRecordingIndicatorVisualRepresentation setBlurRadius:];
-[SBRecordingIndicatorVisualRepresentation indicatorType];
-[SBRecordingIndicatorVisualRepresentation viewType];
-[SBRecordingIndicatorVisualRepresentation _indicatorColorForIndicatorType:];
-[SBRecordingIndicatorVisualRepresentation _updateHighLevelLayerIndicatorType:];
-[SBRecordingIndicatorVisualRepresentation highLevelLayer];
-[SBRecordingIndicatorVisualRepresentation highLevelView];
-[SBRecordingIndicatorVisualRepresentation initWithViewType:usesHighLevelView:];
```
