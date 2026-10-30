# `CFXPickerSession`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 16 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _isCompactPresentation;
B _didScroll;
B _didModifyEffectsStack;
B _didRemoveEffect;
@"NSString" _pickerBundleIdentifier;
d _compactPresentationDuration;
d _expandedPresentationDuration;
@"NSDate" _sessionStartTime;
@"NSDate" _lastCompactPresentationTime;
@"NSDate" _lastExpandedPresentationTime;
^d _totalCompactPresentationDuration;
^d _totalExpandedPresentationDuration;
@"NSString" _typeOfRemovedEffect;
```

## Properties

```
@property (T@"NSDate",R,N,V_sessionStartTime) sessionStartTime;
@property (T@"NSDate",N,V_lastCompactPresentationTime) lastCompactPresentationTime;
@property (T@"NSDate",N,V_lastExpandedPresentationTime) lastExpandedPresentationTime;
@property (T^d,N,V_totalCompactPresentationDuration) totalCompactPresentationDuration;
@property (T^d,N,V_totalExpandedPresentationDuration) totalExpandedPresentationDuration;
@property (TB,N,V_didModifyEffectsStack) didModifyEffectsStack;
@property (TB,N,V_didRemoveEffect) didRemoveEffect;
@property (T@"NSString",N,V_typeOfRemovedEffect) typeOfRemovedEffect;
@property (T@"NSString",R,N,V_pickerBundleIdentifier) pickerBundleIdentifier;
@property (Td,R,N) sessionDuration;
@property (TB,R,N,V_isCompactPresentation) isCompactPresentation;
@property (TB,R,N) isExpandedPresentation;
@property (Td,R,N,V_compactPresentationDuration) compactPresentationDuration;
@property (Td,R,N,V_expandedPresentationDuration) expandedPresentationDuration;
@property (TB,N,V_didScroll) didScroll;
@property (T@"NSDictionary",R,N) effectChangesDict;
```

## Instance methods

```
-[CFXPickerSession didDismiss];
-[CFXPickerSession sessionDuration];
-[CFXPickerSession didScroll];
-[CFXPickerSession sessionStartTime];
-[CFXPickerSession didRemoveEffect];
-[CFXPickerSession setLastCompactPresentationTime:];
-[CFXPickerSession compactPresentationDuration];
-[CFXPickerSession didChangePresentationMode];
-[CFXPickerSession didModifyEffectOfType:wasRemoval:];
-[CFXPickerSession didModifyEffectsStack];
-[CFXPickerSession effectChangesDict];
-[CFXPickerSession expandedPresentationDuration];
-[CFXPickerSession initWithIdentifier:isCompact:];
-[CFXPickerSession isCompactPresentation];
-[CFXPickerSession isExpandedPresentation];
-[CFXPickerSession lastCompactPresentationTime];
-[CFXPickerSession lastExpandedPresentationTime];
-[CFXPickerSession pickerBundleIdentifier];
-[CFXPickerSession setDidModifyEffectsStack:];
-[CFXPickerSession setDidRemoveEffect:];
-[CFXPickerSession setDidScroll:];
-[CFXPickerSession setLastExpandedPresentationTime:];
-[CFXPickerSession setTotalCompactPresentationDuration:];
-[CFXPickerSession setTotalExpandedPresentationDuration:];
-[CFXPickerSession setTypeOfRemovedEffect:];
-[CFXPickerSession totalCompactPresentationDuration];
-[CFXPickerSession totalExpandedPresentationDuration];
-[CFXPickerSession typeOfRemovedEffect];
```
