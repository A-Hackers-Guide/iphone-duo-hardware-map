# `_UIInertPreviewingContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerPreviewing_Internal`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIGestureRecognizer" _failureRelationshipGestureRecognizer;
@"<UIViewControllerPreviewingDelegate>" _delegate;
@"UIView" _customViewForInteractiveHighlight;
@"UIView" _sourceView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T@"UIView",&,N,V_sourceView) sourceView;
@property (T@"<UIViewControllerPreviewingDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N,V_customViewForInteractiveHighlight) customViewForInteractiveHighlight;
@property (T@"UIGestureRecognizer",R,N) previewingGestureRecognizerForFailureRelationship;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceRect) sourceRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInertPreviewingContext setSourceRect:];
-[_UIInertPreviewingContext sourceRect];
-[_UIInertPreviewingContext initWithSourceView:];
-[_UIInertPreviewingContext unregister];
-[_UIInertPreviewingContext setDelegate:];
-[_UIInertPreviewingContext setSourceView:];
-[_UIInertPreviewingContext delegate];
-[_UIInertPreviewingContext sourceView];
-[_UIInertPreviewingContext customViewForInteractiveHighlight];
-[_UIInertPreviewingContext preferredSourceViewRectInCoordinateSpace:];
-[_UIInertPreviewingContext previewingGestureRecognizerForFailureRelationship];
-[_UIInertPreviewingContext setCustomViewForInteractiveHighlight:];
```
