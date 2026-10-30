# `TCPhraseCollector`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
B _valid;
```

## Class methods

```
+[TCPhraseCollector sharedInstance];
```

## Instance methods

```
-[TCPhraseCollector init];
-[TCPhraseCollector setValid:];
-[TCPhraseCollector isValid];
-[TCPhraseCollector connection];
-[TCPhraseCollector _initConnection];
-[TCPhraseCollector collectSentence:language:phraseRanges:];
```
