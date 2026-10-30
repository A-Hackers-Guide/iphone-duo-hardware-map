# `PKColorPicker`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_PKColorPickerViewDelegate`
- 2 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"<PKColorPickerDelegate>" _delegate;
@"_PKColorPickerView" _colorPickerView;
```

## Properties

```
@property (T@"_PKColorPickerView",&,N,V_colorPickerView) colorPickerView;
@property (T@"<PKColorPickerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIColor",&,N) selectedColor;
@property (Tq,N) colorUserInterfaceStyle;
@property (TB,N) colorUserInterfaceStyleOnlyConvertsBlackAndWhite;
```

## Class methods

```
+[PKColorPicker _representableColorForColor:];
```

## Instance methods

```
-[PKColorPicker init];
-[PKColorPicker viewDidLoad];
-[PKColorPicker _canShowWhileLocked];
-[PKColorPicker setDelegate:];
-[PKColorPicker delegate];
-[PKColorPicker viewWillLayoutSubviews];
-[PKColorPicker preferredContentSize];
-[PKColorPicker selectedColor];
-[PKColorPicker setSelectedColor:];
-[PKColorPicker setColorUserInterfaceStyle:];
-[PKColorPicker colorPickerView];
-[PKColorPicker _colorPickerView];
-[PKColorPicker _colorPickerViewDidChangeSelectedColor:];
-[PKColorPicker _colorPickerViewUserDidTouchUpInside:];
-[PKColorPicker _setInitialColorForSpringLoading:];
-[PKColorPicker _setSelectedColorForPoint:];
-[PKColorPicker colorUserInterfaceStyle];
-[PKColorPicker colorUserInterfaceStyleOnlyConvertsBlackAndWhite];
-[PKColorPicker setColorPickerView:];
-[PKColorPicker setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:];
```
