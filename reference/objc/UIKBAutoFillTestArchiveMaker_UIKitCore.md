# `UIKBAutoFillTestArchiveMaker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSKeyedArchiverDelegate`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"UIKBAutoFillTestArchive" _testArchive;
@"UIViewController" _viewControllerToSnapshot;
q _currentTableViewTag;
q _currentTextFieldTag;
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
+[UIKBAutoFillTestArchiveMaker archiveMakerWithViewControllerToSnapshot:];
```

## Instance methods

```
-[UIKBAutoFillTestArchiveMaker archiver:willEncodeObject:];
-[UIKBAutoFillTestArchiveMaker _cloneTextView:];
-[UIKBAutoFillTestArchiveMaker _applyPropertiesFromLabel:toLabel:];
-[UIKBAutoFillTestArchiveMaker _applyPropertiesFromView:toView:];
-[UIKBAutoFillTestArchiveMaker _cloneBarButtonItem:];
-[UIKBAutoFillTestArchiveMaker _cloneButton:];
-[UIKBAutoFillTestArchiveMaker _cloneGenericView:];
-[UIKBAutoFillTestArchiveMaker _cloneLabel:];
-[UIKBAutoFillTestArchiveMaker _cloneNavigationItem:];
-[UIKBAutoFillTestArchiveMaker _cloneTableView:];
-[UIKBAutoFillTestArchiveMaker _cloneTextField:];
-[UIKBAutoFillTestArchiveMaker _cloneView:];
-[UIKBAutoFillTestArchiveMaker _cloneViewHierarchyFromRootView:];
-[UIKBAutoFillTestArchiveMaker _makeCopyOfObject:];
-[UIKBAutoFillTestArchiveMaker initWithViewControllerToSnapshot:];
-[UIKBAutoFillTestArchiveMaker makeArchive];
```
