# `PKInkFunction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 28 instance methods, 0 class methods

## Instance variables

```
Q _inkProperty;
Q _inkInput;
Q _inputMask;
Q _deviceMask;
Q _math;
@"NSMutableArray" _inputPoints;
@"NSMutableArray" _minOutputPoints;
@"NSMutableArray" _maxOutputPoints;
@"NSMutableArray" _outputPoints;
Q _functionType;
@"NSMutableArray" _controlPoints;
@"NSMutableArray" _maxInputPoints;
```

## Properties

```
@property (TQ,N,V_inkProperty) inkProperty;
@property (TQ,N,V_inkInput) inkInput;
@property (TQ,N,V_inputMask) inputMask;
@property (TQ,N,V_deviceMask) deviceMask;
@property (TQ,N,V_math) math;
@property (T@"NSMutableArray",&,N,V_inputPoints) inputPoints;
@property (T@"NSMutableArray",&,N,V_maxInputPoints) maxInputPoints;
@property (T@"NSMutableArray",&,N,V_minOutputPoints) minOutputPoints;
@property (T@"NSMutableArray",&,N,V_maxOutputPoints) maxOutputPoints;
@property (T@"NSMutableArray",&,N,V_outputPoints) outputPoints;
@property (TQ,N,V_functionType) functionType;
@property (T@"NSMutableArray",&,N,V_controlPoints) controlPoints;
```

## Instance methods

```
-[PKInkFunction functionType];
-[PKInkFunction controlPoints];
-[PKInkFunction description];
-[PKInkFunction deviceMask];
-[PKInkFunction setDeviceMask:];
-[PKInkFunction setControlPoints:];
-[PKInkFunction inputMask];
-[PKInkFunction setInputMask:];
-[PKInkFunction setInputPoints:];
-[PKInkFunction inputPoints];
-[PKInkFunction minOutputPoints];
-[PKInkFunction maxOutputPoints];
-[PKInkFunction setInkProperty:];
-[PKInkFunction initWithInputPoints:outputPoints:functionType:];
-[PKInkFunction initWithProperty:input:math:inputMask:deviceMask:inputPoints:maxInputPoints:minOutputPoints:maxOutputPoints:outputPoints:controlPoints:functionType:];
-[PKInkFunction inkInput];
-[PKInkFunction inkProperty];
-[PKInkFunction math];
-[PKInkFunction maxInputPoints];
-[PKInkFunction outputPoints];
-[PKInkFunction setFunctionType:];
-[PKInkFunction setInkInput:];
-[PKInkFunction setMath:];
-[PKInkFunction setMaxInputPoints:];
-[PKInkFunction setMaxOutputPoints:];
-[PKInkFunction setMinOutputPoints:];
-[PKInkFunction setOutputPoints:];
-[PKInkFunction solveForInput:];
```
