# EZCBL - Easy COBOL

A modern DSL (Domain-Specific Language) that compiles to COBOL, designed to reduce boilerplate and make COBOL development more accessible.

## Why?

COBOL is verbose. Really verbose. A simple module call can require 10+ lines of boilerplate code. EZCBL lets you write clean, readable code that compiles to standard COBOL.

**Before (COBOL):**
```cobol
      PERFORM CALL-CUSTOMER-VALIDATE
      
      CALL-CUSTOMER-VALIDATE.
          MOVE CUST-ID
            TO PARAM-1 OF WS-PARAMS
            
          MOVE CUST-NAME
            TO PARAM-2 OF WS-PARAMS
            
          MOVE STATUS-CODE
            TO PARAM-3 OF WS-PARAMS
            
          CALL 'CUSTOMER_VALIDATE' USING WS-PARAMS

          IF TRUE OF ERRSTS OF WS-PARAMS
              PERFORM ERR-CALL-CUSTOMER-VALIDATE
          END-IF
          .

      CALL-ERRMODUL-BLOCKING.
          SET BLOCKING OF ERRTYP OF WS-ERRMODUL
           TO TRUE

          CALL ERRMODUL USING WS-ERRMODUL

          PERFORM 9000-END-PROGRAM
      .

      ERR-CALL-CUSTOMER-VALIDATE.
          MOVE ERRCODE-1000
            TO ERRCODE OF WS-ERRMODUL

          PERFORM CALL-ERRMODUL-BLOCKING
          .

      9000-END-PROGRAM.
          GOBACK
          .
```

**After (EZCBL):**
```ezcbl
CUSTOMER_VALIDATE(CUST-ID, CUST-NAME, STATUS-CODE)
```

## Status

🚀 **v0.2 - Working Prototype**

Currently implemented:
- ✅ Basic function call syntax
- ✅ Multiple function calls per file
- ✅ Automatic Working-Storage literal generation
- ✅ File output (.ezcbl → .cbl)
- ✅ Proper COBOL structure (DATA/PROCEDURE DIVISION)
- ✅ Generated code header with timestamp

Try it:
```bash
python ezcbl.py yourfile.ezcbl
# Generates yourfile.cbl
```

## Roadmap

- [x] Basic function call syntax
- [x] File output generation
- [x] Working-Storage literal generation
- [x] Multiple function calls per file
- [ ] Main program flow / paragraph sequencing
- [ ] Variable declarations
- [ ] Control flow (if/switch)
- [ ] Error handling boilerplate
- [ ] Function-code module abstraction
- [ ] VSCode extension

## Philosophy

- **Commit both versions**: Both EZCBL and generated COBOL are version controlled
- **Incremental adoption**: Use alongside existing COBOL code
- **Readable intent**: Code that's obvious to read, even for non-COBOL developers
- **AI-friendly**: Simpler syntax makes LLM-assisted development feasible

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

For commercial licensing options, please contact leo.calendini-pro@yahoo.com.
