# `UIDragPreview`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 8 properties, 16 instance methods, 5 class methods

## Instance variables

```
@"NSValue" _preferredAnchorPoint;
B _preventAfterScreenUpdatesSnapshot;
B _avoidAnimation;
@"UIView" _view;
@"UIDragPreviewParameters" _parameters;
@"NSDictionary" __springboardParameters;
```

## Properties

```
@property (TB,N,G_preventAfterScreenUpdatesSnapshot,S_setPreventAfterScreenUpdatesSnapshot:,V_preventAfterScreenUpdatesSnapshot) preventAfterScreenUpdatesSnapshot;
@property (TB,N,V_avoidAnimation) avoidAnimation;
@property (T{CGPoint=dd},N) preferredAnchorPoint;
@property (T@"_DUIPreview",R,N) _duiPreview;
@property (TB,N) _springboardPlatterStyle;
@property (T@"NSDictionary",C,N,V__springboardParameters) _springboardParameters;
@property (T@"UIView",R,N,V_view) view;
@property (T@"UIDragPreviewParameters",R,C,N,V_parameters) parameters;
```

## Class methods

```
+[UIDragPreview _previewWithHiddenViewDuringDrag:placeholderSize:parameters:];
+[UIDragPreview defaultBoundingSize];
+[UIDragPreview previewForURL:];
+[UIDragPreview previewForURL:title:];
+[UIDragPreview textBoundingSize];
```

## Instance methods

```
-[UIDragPreview parameters];
-[UIDragPreview initWithView:];
-[UIDragPreview set_springboardParameters:];
-[UIDragPreview _springboardParameters];
-[UIDragPreview _setPreventAfterScreenUpdatesSnapshot:];
-[UIDragPreview view];
-[UIDragPreview _preventAfterScreenUpdatesSnapshot];
-[UIDragPreview _springboardPlatterStyle];
-[UIDragPreview _duiPreview];
-[UIDragPreview copyWithZone:];
-[UIDragPreview set_springboardPlatterStyle:];
-[UIDragPreview initWithView:parameters:];
-[UIDragPreview avoidAnimation];
-[UIDragPreview preferredAnchorPoint];
-[UIDragPreview setAvoidAnimation:];
-[UIDragPreview setPreferredAnchorPoint:];
```
