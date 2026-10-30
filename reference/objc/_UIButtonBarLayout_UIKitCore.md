# `_UIButtonBarLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 5 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"<_UIButtonBarLayoutMetricsData>" _layoutMetrics;
B _dirty;
```

## Properties

```
@property (TB,N,GisDirty,V_dirty) dirty;
@property (TB,R,N) isSpaceLayout;
@property (TB,R,N) isGroupLayout;
@property (T@"UIBarButtonItem",R,N) barButtonItem;
@property (T@"NSArray",R,N) subLayouts;
```

## Instance methods

```
-[_UIButtonBarLayout _configure];
-[_UIButtonBarLayout configure];
-[_UIButtonBarLayout setDirty:];
-[_UIButtonBarLayout init];
-[_UIButtonBarLayout barButtonItem];
-[_UIButtonBarLayout description];
-[_UIButtonBarLayout compact];
-[_UIButtonBarLayout isDirty];
-[_UIButtonBarLayout addLayoutViews:];
-[_UIButtonBarLayout suppressSpacing];
-[_UIButtonBarLayout _addConstraintsToActivate:toDeactivate:];
-[_UIButtonBarLayout _addLayoutGuides:];
-[_UIButtonBarLayout _addLayoutViews:];
-[_UIButtonBarLayout _metricsData];
-[_UIButtonBarLayout _shouldBeDirty];
-[_UIButtonBarLayout addConstraintsToActivate:toDeactivate:];
-[_UIButtonBarLayout addLayoutGuides:];
-[_UIButtonBarLayout addLayoutViews:layoutGuides:constraintsToActivate:constraintsToDeactivate:];
-[_UIButtonBarLayout dirtyLayoutForPlainAppearanceChange:doneAppearanceChanged:];
-[_UIButtonBarLayout initWithLayoutMetrics:];
-[_UIButtonBarLayout isGroupLayout];
-[_UIButtonBarLayout isSpaceLayout];
-[_UIButtonBarLayout minimumLayoutWidthGivenMinimumSpaceWidth:];
-[_UIButtonBarLayout setSuppressSpacing:];
-[_UIButtonBarLayout setUseGroupSizing:];
-[_UIButtonBarLayout shouldHorizontallyCenterView:];
-[_UIButtonBarLayout subLayouts];
-[_UIButtonBarLayout useGroupSizing];
```
