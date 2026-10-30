# `SBFBuildVersion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _stringRepresentation;
q _majorBuildNumber;
@"NSString" _majorBuildLetterString;
q _minorBuildNumber;
@"NSString" _minorBuildLetterString;
```

## Properties

```
@property (T@"NSString",R,C,N,V_stringRepresentation) stringRepresentation;
@property (Tq,R,N,V_majorBuildNumber) majorBuildNumber;
@property (T@"NSString",R,C,N,V_majorBuildLetterString) majorBuildLetterString;
@property (Tq,R,N,V_minorBuildNumber) minorBuildNumber;
@property (T@"NSString",R,C,N,V_minorBuildLetterString) minorBuildLetterString;
```

## Instance methods

```
-[SBFBuildVersion initWithString:];
-[SBFBuildVersion stringRepresentation];
-[SBFBuildVersion hash];
-[SBFBuildVersion description];
-[SBFBuildVersion isEqual:];
-[SBFBuildVersion majorBuildLetterString];
-[SBFBuildVersion majorBuildNumber];
-[SBFBuildVersion minorBuildLetterString];
-[SBFBuildVersion minorBuildNumber];
-[SBFBuildVersion compareBuildVersion:withPrecision:];
-[SBFBuildVersion compareBuildVersionString:withPrecision:];
```
