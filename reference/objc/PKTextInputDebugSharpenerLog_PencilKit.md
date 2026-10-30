# `PKTextInputDebugSharpenerLog`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _logEntries;
@"NSDictionary" _metadataDictionary;
```

## Properties

```
@property (T@"NSArray",R,N,V_logEntries) logEntries;
@property (T@"NSDictionary",R,N,V_metadataDictionary) metadataDictionary;
@property (TB,R,N) hasContent;
```

## Class methods

```
+[PKTextInputDebugSharpenerLog _environmentMetadataDictionary];
+[PKTextInputDebugSharpenerLog _recommendedFileNameForLogWithDate:];
+[PKTextInputDebugSharpenerLog canLoadFromFileAtURL:];
```

## Instance methods

```
-[PKTextInputDebugSharpenerLog initWithContentsOfURL:error:];
-[PKTextInputDebugSharpenerLog description];
-[PKTextInputDebugSharpenerLog _loadFromFileURL:error:];
-[PKTextInputDebugSharpenerLog hasContent];
-[PKTextInputDebugSharpenerLog metadataDictionary];
-[PKTextInputDebugSharpenerLog logEntries];
-[PKTextInputDebugSharpenerLog _dictionaryRepresentationWithContentLevel:excludeEntyIndexes:];
-[PKTextInputDebugSharpenerLog initWithLogEntries:];
-[PKTextInputDebugSharpenerLog writeLogToTemporaryDirectoryWithContentLevel:excludeEntyIndexes:error:];
-[PKTextInputDebugSharpenerLog writeToURL:withContentLevel:excludeEntyIndexes:error:];
```
