# `_UISheetDropInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropInteractionDelegate`, `UIInteraction`
- 5 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<_UISheetDropInteractionDelegate>" _delegate;
@"UIDropInteraction" _dropInteraction;
@"NSMapTable" _activityTypesOrActivities;
@"UIPresentationController" _presentationController;
```

## Properties

```
@property (T@"UIDropInteraction",R,N,V_dropInteraction) dropInteraction;
@property (T@"NSMapTable",R,N,V_activityTypesOrActivities) activityTypesOrActivities;
@property (T@"UIPresentationController",&,N,V_presentationController) presentationController;
@property (T@"<_UISheetDropInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UISheetDropInteraction dropInteraction:sessionDidUpdate:];
-[_UISheetDropInteraction initWithDelegate:];
-[_UISheetDropInteraction dropInteraction:performDrop:];
-[_UISheetDropInteraction dropInteraction];
-[_UISheetDropInteraction dropInteraction:canHandleSession:];
-[_UISheetDropInteraction dropInteraction:item:willAnimateDropWithAnimator:];
-[_UISheetDropInteraction view];
-[_UISheetDropInteraction willMoveToView:];
-[_UISheetDropInteraction presentationController];
-[_UISheetDropInteraction delegate];
-[_UISheetDropInteraction setPresentationController:];
-[_UISheetDropInteraction dropInteraction:sessionDidEnd:];
-[_UISheetDropInteraction didMoveToView:];
-[_UISheetDropInteraction dropInteraction:previewForDroppingItem:withDefault:];
-[_UISheetDropInteraction _activityForSession:completion:];
-[_UISheetDropInteraction _activityTypeForSession:];
-[_UISheetDropInteraction _removeActivityTypeOrActivityForSession:];
-[_UISheetDropInteraction activityTypesOrActivities];
```
