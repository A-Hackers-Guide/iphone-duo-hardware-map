# `_UIDatePickerLinkedLabelStorage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _sizingLabel;
@"NSHashTable" _attachedLabels;
Q _currentPriority;
@"NSCache" _sizeCache;
```

## Instance methods

```
-[_UIDatePickerLinkedLabelStorage init];
-[_UIDatePickerLinkedLabelStorage _resetPriority];
-[_UIDatePickerLinkedLabelStorage _attachLabel:];
-[_UIDatePickerLinkedLabelStorage _cachedSizeForKey:size:];
-[_UIDatePickerLinkedLabelStorage _currentPriority];
-[_UIDatePickerLinkedLabelStorage _detachLabel:];
-[_UIDatePickerLinkedLabelStorage _notifyAllLabelsExcept:];
-[_UIDatePickerLinkedLabelStorage _setCachedSize:forKey:];
-[_UIDatePickerLinkedLabelStorage _setPriority:label:];
-[_UIDatePickerLinkedLabelStorage _sizeForText:font:height:overrideAttributes:];
```
