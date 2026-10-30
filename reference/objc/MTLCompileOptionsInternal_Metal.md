# `MTLCompileOptionsInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLCompileOptions`
- 22 instance variables, 0 properties, 53 instance methods, 0 class methods

## Instance variables

```
B _userSetLanguageVersion;
@"NSDictionary" _preprocessorMacros;
q _mathMode;
q _mathFloatingPointFunctions;
B _glBufferBindPoints;
B _tracingEnabled;
B _debuggingEnabled;
Q _languageVersion;
B _compileTimeStatisticsEnabled;
@"NSString" _additionalCompilerArguments;
C _sourceLanguage;
q _libraryType;
@"NSArray" _libraries;
@"NSString" _installName;
B _preserveInvariance;
q _optimizationLevel;
q _compileSymbolVisibility;
B _allowReferencingUndefinedSymbols;
Q _maxTotalThreadsPerThreadgroup;
B _enableLogging;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerThreadgroup;
q _floatingPointConversionRoundingMode;
```

## Instance methods

```
-[MTLCompileOptionsInternal floatingPointConversionRoundingMode];
-[MTLCompileOptionsInternal compileTimeStatisticsEnabled];
-[MTLCompileOptionsInternal setRequiredThreadsPerThreadgroup:];
-[MTLCompileOptionsInternal setLibraryType:];
-[MTLCompileOptionsInternal formattedDescription:];
-[MTLCompileOptionsInternal fastMathEnabled];
-[MTLCompileOptionsInternal importDictionary:];
-[MTLCompileOptionsInternal init];
-[MTLCompileOptionsInternal mathMode];
-[MTLCompileOptionsInternal setMathMode:];
-[MTLCompileOptionsInternal exportDictionary];
-[MTLCompileOptionsInternal dealloc];
-[MTLCompileOptionsInternal setGlBufferBindPoints:];
-[MTLCompileOptionsInternal setLanguageVersion:];
-[MTLCompileOptionsInternal preserveInvariance];
-[MTLCompileOptionsInternal enableLogging];
-[MTLCompileOptionsInternal tracingEnabled];
-[MTLCompileOptionsInternal setAdditionalCompilerArguments:];
-[MTLCompileOptionsInternal glBufferBindPoints];
-[MTLCompileOptionsInternal setFastMathEnabled:];
-[MTLCompileOptionsInternal setFloatingPointConversionRoundingMode:];
-[MTLCompileOptionsInternal setMaxTotalThreadsPerThreadgroup:];
-[MTLCompileOptionsInternal setCompileSymbolVisibility:];
-[MTLCompileOptionsInternal setOptimizationLevel:];
-[MTLCompileOptionsInternal requiredThreadsPerThreadgroup];
-[MTLCompileOptionsInternal maxTotalThreadsPerThreadgroup];
-[MTLCompileOptionsInternal optimizationLevel];
-[MTLCompileOptionsInternal installName];
-[MTLCompileOptionsInternal setSourceLanguage:];
-[MTLCompileOptionsInternal setLibraries:];
-[MTLCompileOptionsInternal additionalCompilerArguments];
-[MTLCompileOptionsInternal setEnableLogging:];
-[MTLCompileOptionsInternal setDebuggingEnabled:];
-[MTLCompileOptionsInternal sourceLanguage];
-[MTLCompileOptionsInternal libraryType];
-[MTLCompileOptionsInternal hash];
-[MTLCompileOptionsInternal debuggingEnabled];
-[MTLCompileOptionsInternal description];
-[MTLCompileOptionsInternal libraries];
-[MTLCompileOptionsInternal setAllowReferencingUndefinedSymbols:];
-[MTLCompileOptionsInternal setMathFloatingPointFunctions:];
-[MTLCompileOptionsInternal setInstallName:];
-[MTLCompileOptionsInternal setTracingEnabled:];
-[MTLCompileOptionsInternal setPreprocessorMacros:];
-[MTLCompileOptionsInternal copyWithZone:];
-[MTLCompileOptionsInternal mathFloatingPointFunctions];
-[MTLCompileOptionsInternal compileSymbolVisibility];
-[MTLCompileOptionsInternal languageVersion];
-[MTLCompileOptionsInternal allowReferencingUndefinedSymbols];
-[MTLCompileOptionsInternal isEqual:];
-[MTLCompileOptionsInternal preprocessorMacros];
-[MTLCompileOptionsInternal setPreserveInvariance:];
-[MTLCompileOptionsInternal setCompileTimeStatisticsEnabled:];
```
