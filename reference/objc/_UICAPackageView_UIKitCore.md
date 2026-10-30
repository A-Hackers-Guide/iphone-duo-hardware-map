# `_UICAPackageView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 2 instance variables, 0 properties, 4 instance methods, 5 class methods

## Instance variables

```
@"CAPackage" _package;
@"NSArray" _rootViews;
```

## Class methods

```
+[_UICAPackageView loadPackageViewWithData:publishedObjectViewClassMap:completion:];
+[_UICAPackageView _newViewHierarchyFrom:publishedObjectViewClassMap:into:];
+[_UICAPackageView _shouldCatchDecodingExceptions];
+[_UICAPackageView loadPackageViewWithContentsOfURL:publishedObjectViewClassMap:completion:];
+[_UICAPackageView loadPackageViewWithObject:publishedObjectViewClassMap:completion:];
```

## Instance methods

```
-[_UICAPackageView initWithContentsOfURL:publishedObjectViewClassMap:];
-[_UICAPackageView publishedObjectWithName:];
-[_UICAPackageView initWithData:publishedObjectViewClassMap:];
-[_UICAPackageView publishedViewWithName:];
```
