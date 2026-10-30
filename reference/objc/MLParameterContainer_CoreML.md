# `MLParameterContainer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _currentParameterValues;
@"NSArray" _parameterKeys;
@"NSDictionary" _parameterDescriptions;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_currentParameterValues) currentParameterValues;
@property (T@"NSArray",&,N,V_parameterKeys) parameterKeys;
@property (T@"NSDictionary",&,N,V_parameterDescriptions) parameterDescriptions;
```

## Class methods

```
+[MLParameterContainer supportsSecureCoding];
+[MLParameterContainer parameterContainerFor:descriptions:];
```

## Instance methods

```
-[MLParameterContainer encodeWithCoder:];
-[MLParameterContainer description];
-[MLParameterContainer initWithCoder:];
-[MLParameterContainer currentParameterValues];
-[MLParameterContainer parameterDescriptions];
-[MLParameterContainer parameterKeys];
-[MLParameterContainer setCurrentParameterValues:];
-[MLParameterContainer setCurrentValue:forKey:error:];
-[MLParameterContainer setParameterDescriptions:];
-[MLParameterContainer setParameterKeys:];
-[MLParameterContainer validateParameterValue:givenConstraint:];
```
