# `_UIFieldEditorHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"UIView<_UIFieldEditorHostingViewRequirements>" _hostingView;
@"UIFieldEditor" _hostedFieldEditor;
```

## Properties

```
@property (T@"UIView<_UIFieldEditorHostingViewRequirements>",R,W,N,V_hostingView) hostingView;
@property (T@"UIFieldEditor",R,N,V_hostedFieldEditor) hostedFieldEditor;
@property (TB,R,N,GisHostingFieldEditor) hostingFieldEditor;
```

## Class methods

```
+[_UIFieldEditorHost fieldEditorHostForTextField:];
```

## Instance methods

```
-[_UIFieldEditorHost layoutIfNeeded];
-[_UIFieldEditorHost addFieldEditor:];
-[_UIFieldEditorHost hostingView];
-[_UIFieldEditorHost initWithHostingView:];
-[_UIFieldEditorHost isHostingFieldEditor];
-[_UIFieldEditorHost _viewForHostingFieldEditor];
-[_UIFieldEditorHost description];
-[_UIFieldEditorHost hostedFieldEditor];
-[_UIFieldEditorHost removeFieldEditor];
-[_UIFieldEditorHost addPlaceholderLabel:];
```
