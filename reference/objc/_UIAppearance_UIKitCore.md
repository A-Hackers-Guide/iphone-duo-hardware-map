# `_UIAppearance`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 15 instance methods, 23 class methods

## Instance variables

```
@"NSArray" _containerList;
@"NSMutableArray" _appearanceInvocations;
@"NSMapTable" _invocationSources;
@"_UIAppearanceCustomizableClassInfo" _customizableClassInfo;
```

## Properties

```
@property (T@"_UIAppearanceCustomizableClassInfo",R,N,V_customizableClassInfo) _customizableClassInfo;
```

## Class methods

```
+[_UIAppearance recursiveDescription];
+[_UIAppearance _hasAnyCustomizations];
+[_UIAppearance _rootAppearancesNode];
+[_UIAppearance _applyInvocationsTo:window:matchingSelector:onlySystemInvocations:];
+[_UIAppearance _pendingRecordInvocationsForSource:];
+[_UIAppearance _newAppearanceWithClassInfo:containerList:];
+[_UIAppearance _recordersExcludingSource:withWindow:];
+[_UIAppearance _currentAppearanceSource];
+[_UIAppearance _setInvalidatesViewsOnAppearanceChange:];
+[_UIAppearance _appearanceWithClassInfo:containerList:];
+[_UIAppearance _hasCustomizationsForClass:guideClass:];
+[_UIAppearance _addWindow:forSource:];
+[_UIAppearance _appendDescriptionOfNode:toString:atLevel:];
+[_UIAppearance _removeWindow:forSource:];
+[_UIAppearance _appearanceForClass:withContainerList:];
+[_UIAppearance _recorderForSource:];
+[_UIAppearance _removeInvocationsForSource:];
+[_UIAppearance _windowsForSource:];
+[_UIAppearance appearancesAtNode:withObject:];
+[_UIAppearance _applyInvocationsTo:window:matchingSelector:];
+[_UIAppearance _applyInvocationsTo:window:];
+[_UIAppearance _setCurrentAppearanceSource:];
+[_UIAppearance _appearanceNodeForClassInfo:containerList:];
```

## Instance methods

```
-[_UIAppearance dealloc];
-[_UIAppearance _isRecordingInvocations];
-[_UIAppearance _appearanceInvocations];
-[_UIAppearance _beginListeningForAppearanceEventsForSetter:];
-[_UIAppearance _handleGetterInvocation:];
-[_UIAppearance _customizableClassInfo];
-[_UIAppearance _handleSetterInvocation:];
-[_UIAppearance _removeInvocationsForSource:];
-[_UIAppearance methodSignatureForSelector:];
-[_UIAppearance _traitCollection];
-[_UIAppearance description];
-[_UIAppearance _appendDescriptionToString:atLevel:];
-[_UIAppearance forwardInvocation:];
-[_UIAppearance _invalidateAppearanceInWindow:];
-[_UIAppearance _isValidAppearanceForCustomizableObject:];
```
