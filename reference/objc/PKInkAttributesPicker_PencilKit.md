# `PKInkAttributesPicker`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteAttributeViewController`
- Protocols: `UIPopoverPresentationControllerDelegate`, `_PKInkAttributesPickerViewDelegate`
- 7 instance variables, 12 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"UIStackView" _stackView;
@"UIView" _topViewControllerViewWrapper;
B _updatingOpacityValue;
@"UIViewController" _topViewController;
@"<PKInkAttributesPickerDelegate>" _delegate;
@"_PKInkAttributesPickerView" _pickerView;
d _minimumOpacityValue;
```

## Properties

```
@property (T@"_PKInkAttributesPickerView",&,N,V_pickerView) pickerView;
@property (TQ,N) displayMode;
@property (Td,N,V_minimumOpacityValue) minimumOpacityValue;
@property (TB,R,N,GisUpdatingOpacityValue,V_updatingOpacityValue) updatingOpacityValue;
@property (T@"PKInk",&,N) selectedInk;
@property (T@"<PKInkAttributesPickerDelegate>",&,N,V_delegate) delegate;
@property (Tq,N) colorAppearance;
@property (T@"UIViewController",&,N,V_topViewController) topViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKInkAttributesPicker defaultMinimumOpacityValue];
```

## Instance methods

```
-[PKInkAttributesPicker setDisplayMode:];
-[PKInkAttributesPicker displayMode];
-[PKInkAttributesPicker viewDidLoad];
-[PKInkAttributesPicker _canShowWhileLocked];
-[PKInkAttributesPicker setDelegate:];
-[PKInkAttributesPicker delegate];
-[PKInkAttributesPicker topViewController];
-[PKInkAttributesPicker _updateUI];
-[PKInkAttributesPicker pickerView];
-[PKInkAttributesPicker setPickerView:];
-[PKInkAttributesPicker colorAppearance];
-[PKInkAttributesPicker setSelectedInk:];
-[PKInkAttributesPicker _inkAttributesPickerViewUserDidEndDraggingSlider:];
-[PKInkAttributesPicker _inkAttributesPickerViewUserDidStartDraggingSlider:];
-[PKInkAttributesPicker _notifyInkAttributesPickerDidChangeInk];
-[PKInkAttributesPicker initWithInk:toolConfiguration:];
-[PKInkAttributesPicker inkAttributesPickerViewDidChangeInkAzimuth:];
-[PKInkAttributesPicker inkAttributesPickerViewDidChangeInkOpacity:];
-[PKInkAttributesPicker inkAttributesPickerViewDidChangeInkThickness:];
-[PKInkAttributesPicker isUpdatingOpacityValue];
-[PKInkAttributesPicker minimumOpacityValue];
-[PKInkAttributesPicker selectedInk];
-[PKInkAttributesPicker setColorAppearance:];
-[PKInkAttributesPicker setMinimumOpacityValue:];
-[PKInkAttributesPicker setSelectedInk:animated:];
-[PKInkAttributesPicker setTopViewController:];
```
