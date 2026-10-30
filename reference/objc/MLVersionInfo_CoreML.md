# `MLVersionInfo`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 8 instance methods, 3 class methods

## Instance variables

```
q _majorVersion;
q _minorVersion;
q _patchVersion;
@"NSString" _variantString;
```

## Properties

```
@property (Tq,R,V_majorVersion) majorVersion;
@property (Tq,R,V_minorVersion) minorVersion;
@property (Tq,R,V_patchVersion) patchVersion;
@property (T@"NSString",R,V_variantString) variantString;
@property (T@"NSString",R,N) versionNumberString;
@property (T@"NSString",R,N) versionString;
```

## Class methods

```
+[MLVersionInfo versionInfoWithStringProgressive:];
+[MLVersionInfo versionInfoWithString:];
+[MLVersionInfo versionInfoWithMajor:minor:patch:variant:];
```

## Instance methods

```
-[MLVersionInfo majorVersion];
-[MLVersionInfo versionNumberString];
-[MLVersionInfo versionString];
-[MLVersionInfo patchVersion];
-[MLVersionInfo initWithMajor:minor:patch:variant:];
-[MLVersionInfo olderThan:];
-[MLVersionInfo variantString];
-[MLVersionInfo minorVersion];
```
