# `_ANECompilerAnalytics`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _procedureAnalytics;
@"NSData" _analyticsBuffer;
@"NSNumber" _bufferSizeInBytes;
```

## Properties

```
@property (T@"NSData",R,N,V_analyticsBuffer) analyticsBuffer;
@property (T@"NSNumber",R,N,V_bufferSizeInBytes) bufferSizeInBytes;
@property (T@"NSArray",&,N,V_procedureAnalytics) procedureAnalytics;
```

## Class methods

```
+[_ANECompilerAnalytics new];
+[_ANECompilerAnalytics objectWithBuffer:];
```

## Instance methods

```
-[_ANECompilerAnalytics init];
-[_ANECompilerAnalytics serialize];
-[_ANECompilerAnalytics description];
-[_ANECompilerAnalytics analyticsBuffer];
-[_ANECompilerAnalytics initWithBuffer:];
-[_ANECompilerAnalytics getDataValueAt:];
-[_ANECompilerAnalytics bufferSizeInBytes];
-[_ANECompilerAnalytics dataInfoAt:];
-[_ANECompilerAnalytics getBOOLDataValueAt:];
-[_ANECompilerAnalytics groupInfoAt:];
-[_ANECompilerAnalytics layerInfoAt:];
-[_ANECompilerAnalytics offsetTableAt:count:];
-[_ANECompilerAnalytics populateAnalytics];
-[_ANECompilerAnalytics procedureAnalytics];
-[_ANECompilerAnalytics procedureInfoAt:];
-[_ANECompilerAnalytics setProcedureAnalytics:];
-[_ANECompilerAnalytics stringForAnalyticsType:];
-[_ANECompilerAnalytics taskInfoAt:];
```
