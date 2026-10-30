# `MTLCompileOptions`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 22 properties, 1 instance methods, 2 class methods

## Properties

```
@property (TB,D,N) tracingEnabled;
@property (TB,D,N) glBufferBindPoints;
@property (TB,D,N) debuggingEnabled;
@property (TB,D,N) compileTimeStatisticsEnabled;
@property (T@"NSString",C,D,N) additionalCompilerArguments;
@property (TC,D,N) sourceLanguage;
@property (T@"NSDictionary",C,D,N) preprocessorMacros;
@property (TB,D,N) fastMathEnabled;
@property (Tq,D,N) mathMode;
@property (Tq,D,N) mathFloatingPointFunctions;
@property (TQ,D,N) languageVersion;
@property (Tq,D,N) libraryType;
@property (T@"NSString",C,D,N) installName;
@property (T@"NSArray",C,D,N) libraries;
@property (TB,D,N) preserveInvariance;
@property (Tq,D,N) optimizationLevel;
@property (Tq,D,N) compileSymbolVisibility;
@property (TB,D,N) allowReferencingUndefinedSymbols;
@property (TQ,D,N) maxTotalThreadsPerThreadgroup;
@property (T{?=QQQ},D,N) requiredThreadsPerThreadgroup;
@property (TB,D,N) enableLogging;
@property (Tq,D,N) floatingPointConversionRoundingMode;
```

## Class methods

```
+[MTLCompileOptions allocWithZone:];
+[MTLCompileOptions alloc];
```

## Instance methods

```
-[MTLCompileOptions copyWithZone:];
```
