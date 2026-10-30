# `MLCompilerOptions`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _dryRun;
B _containerIsCloud;
B _trainWithMLCompute;
B _allowsPixelBufferDirectBinding;
B _encryptModel;
B _usesCodeSigningIdentityForEncryption;
B _allowMultipleInputsWithEnumeratedShapes;
i _mlProgramAddDuringCompilationMode;
@"NSString" _platform;
@"NSString" _platformVersion;
@"NSNumber" _keyInfoVersion;
@"NSString" _keyID;
@"NSData" _key;
@"NSData" _iv;
@"NSData" _sinf;
@"NSData" _mlsinf;
@"NSURL" _specURL;
@"NSMutableArray" _warnings;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_warnings) warnings;
@property (TB,V_trainWithMLCompute) trainWithMLCompute;
@property (TB,V_dryRun) dryRun;
@property (T@"NSString",&,V_platform) platform;
@property (T@"NSString",&,V_platformVersion) platformVersion;
@property (TB,V_containerIsCloud) containerIsCloud;
@property (TB,V_allowsPixelBufferDirectBinding) allowsPixelBufferDirectBinding;
@property (TB,V_encryptModel) encryptModel;
@property (T@"NSNumber",C,V_keyInfoVersion) keyInfoVersion;
@property (T@"NSString",C,V_keyID) keyID;
@property (T@"NSData",C,V_key) key;
@property (TB,V_usesCodeSigningIdentityForEncryption) usesCodeSigningIdentityForEncryption;
@property (T@"NSData",C,V_iv) iv;
@property (T@"NSData",C,V_sinf) sinf;
@property (T@"NSData",C,V_mlsinf) mlsinf;
@property (T@"NSURL",C,V_specURL) specURL;
@property (Ti,V_mlProgramAddDuringCompilationMode) mlProgramAddDuringCompilationMode;
@property (TB,V_allowMultipleInputsWithEnumeratedShapes) allowMultipleInputsWithEnumeratedShapes;
```

## Class methods

```
+[MLCompilerOptions defaultOptions];
```

## Instance methods

```
-[MLCompilerOptions keyID];
-[MLCompilerOptions setKeyID:];
-[MLCompilerOptions setWarnings:];
-[MLCompilerOptions setTrainWithMLCompute:];
-[MLCompilerOptions init];
-[MLCompilerOptions platform];
-[MLCompilerOptions setPlatform:];
-[MLCompilerOptions setKey:];
-[MLCompilerOptions warnings];
-[MLCompilerOptions trainWithMLCompute];
-[MLCompilerOptions key];
-[MLCompilerOptions dryRun];
-[MLCompilerOptions iv];
-[MLCompilerOptions setIv:];
-[MLCompilerOptions platformVersion];
-[MLCompilerOptions specURL];
-[MLCompilerOptions allowMultipleInputsWithEnumeratedShapes];
-[MLCompilerOptions allowsPixelBufferDirectBinding];
-[MLCompilerOptions containerIsCloud];
-[MLCompilerOptions encryptModel];
-[MLCompilerOptions keyInfoVersion];
-[MLCompilerOptions mlProgramAddDuringCompilationMode];
-[MLCompilerOptions mlsinf];
-[MLCompilerOptions setAllowMultipleInputsWithEnumeratedShapes:];
-[MLCompilerOptions setAllowsPixelBufferDirectBinding:];
-[MLCompilerOptions setContainerIsCloud:];
-[MLCompilerOptions setDryRun:];
-[MLCompilerOptions setEncryptModel:];
-[MLCompilerOptions setKeyInfoVersion:];
-[MLCompilerOptions setMlProgramAddDuringCompilationMode:];
-[MLCompilerOptions setMlsinf:];
-[MLCompilerOptions setPlatformVersion:];
-[MLCompilerOptions setSinf:];
-[MLCompilerOptions setSpecURL:];
-[MLCompilerOptions setUsesCodeSigningIdentityForEncryption:];
-[MLCompilerOptions sinf];
-[MLCompilerOptions usesCodeSigningIdentityForEncryption];
```
