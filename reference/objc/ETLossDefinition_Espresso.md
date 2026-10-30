# `ETLossDefinition`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSString" _inputName;
@"NSString" _targetInputName;
@"NSString" _lossOutputName;
Q _mode;
@"NSString" _outputName;
```

## Properties

```
@property (T@"NSString",&,V_outputName) outputName;
@property (T@"NSString",R,V_inputName) inputName;
@property (T@"NSString",R,V_targetInputName) targetInputName;
@property (T@"NSString",R,V_lossOutputName) lossOutputName;
@property (TQ,R,V_mode) mode;
```

## Class methods

```
+[ETLossDefinition L2LossWithInputName:targetInputName:lossOutputName:];
+[ETLossDefinition BuiltInLoss:];
+[ETLossDefinition crossEntropyLossWithInputName:targetInputName:lossOutputName:];
```

## Instance methods

```
-[ETLossDefinition mode];
-[ETLossDefinition lossOutputName];
-[ETLossDefinition targetInputName];
-[ETLossDefinition initWithMode:inputName:targetName:lossOutputName:];
-[ETLossDefinition inputName];
-[ETLossDefinition outputName];
-[ETLossDefinition setOutputName:];
```
