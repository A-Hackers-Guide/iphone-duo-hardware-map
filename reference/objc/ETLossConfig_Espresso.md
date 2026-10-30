# `ETLossConfig`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 2 class methods

## Instance variables

```
Q _mode;
@"NSString" _loss_name;
@"NSString" _output_name;
@"NSString" _label_name;
@"NSArray" _label_shape;
@"NSString" _custom_network_path;
```

## Properties

```
@property (TQ,V_mode) mode;
@property (T@"NSString",&,V_loss_name) loss_name;
@property (T@"NSString",&,V_output_name) output_name;
@property (T@"NSString",&,V_label_name) label_name;
@property (T@"NSArray",&,V_label_shape) label_shape;
@property (T@"NSString",&,V_custom_network_path) custom_network_path;
```

## Class methods

```
+[ETLossConfig L2Loss];
+[ETLossConfig softmaxCrossEntropyLoss];
```

## Instance methods

```
-[ETLossConfig setMode:];
-[ETLossConfig mode];
-[ETLossConfig setLabel_shape:];
-[ETLossConfig setOutput_name:];
-[ETLossConfig custom_network_path];
-[ETLossConfig label_name];
-[ETLossConfig label_shape];
-[ETLossConfig loss_name];
-[ETLossConfig output_name];
-[ETLossConfig setCustom_network_path:];
-[ETLossConfig setLabel_name:];
-[ETLossConfig setLoss_name:];
```
