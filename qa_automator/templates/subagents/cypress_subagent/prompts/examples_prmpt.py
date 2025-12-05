"""
Exemplos de testes Cypress para tela de login.
Cada constante representa um arquivo no projeto.
"""

PROJECT_STRUCTURE: str = """
projeto-cypress/
├── cypress/
│   ├── e2e/
│   │   └── login.cy.js
│   ├── fixtures/
│   │   └── users.json
│   ├── support/
│   │   ├── commands.js
│   │   └── e2e.js
│   └── pages/
│       └── LoginPage.js
├── cypress.config.js
└── package.json
"""

CYPRESS_CONFIG: str = """
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    viewportWidth: 1280,
    viewportHeight: 720,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
})
"""

PACKAGE_JSON: str = """
{
  "name": "cypress-login-tests",
  "version": "1.0.0",
  "description": "Testes automatizados de login com Cypress",
  "scripts": {
    "cy:open": "cypress open",
    "cy:run": "cypress run",
    "test": "cypress run --spec 'cypress/e2e/login.cy.js'"
  },
  "devDependencies": {
    "cypress": "^13.6.0"
  }
}
"""

LOGIN_PAGE: str = """
// cypress/pages/LoginPage.js
class LoginPage {
  // Seletores
  elements = {
    emailInput: () => cy.get('[data-cy="email-input"]'),
    passwordInput: () => cy.get('[data-cy="password-input"]'),
    submitButton: () => cy.get('[data-cy="login-button"]'),
    errorMessage: () => cy.get('[data-cy="error-message"]'),
    successMessage: () => cy.get('[data-cy="success-message"]'),
    forgotPasswordLink: () => cy.get('[data-cy="forgot-password"]'),
  }

  // Ações
  visit() {
    cy.visit('/login')
  }

  fillEmail(email) {
    this.elements.emailInput().clear().type(email)
  }

  fillPassword(password) {
    this.elements.passwordInput().clear().type(password)
  }

  clickSubmit() {
    this.elements.submitButton().click()
  }

  login(email, password) {
    this.fillEmail(email)
    this.fillPassword(password)
    this.clickSubmit()
  }

  // Verificações
  verifyErrorMessage(message) {
    this.elements.errorMessage().should('be.visible').and('contain', message)
  }

  verifySuccessfulLogin() {
    cy.url().should('not.include', '/login')
    this.elements.successMessage().should('be.visible')
  }
}

export default new LoginPage()
"""

USERS_FIXTURE: str = """
{
  "validUser": {
    "email": "usuario@exemplo.com",
    "password": "Senha123!"
  },
  "invalidUser": {
    "email": "invalido@exemplo.com",
    "password": "senhaErrada"
  },
  "emptyCredentials": {
    "email": "",
    "password": ""
  }
}
"""

CUSTOM_COMMANDS: str = """
// cypress/support/commands.js

// Comando customizado para login
Cypress.Commands.add('login', (email, password) => {
  cy.visit('/login')
  cy.get('[data-cy="email-input"]').type(email)
  cy.get('[data-cy="password-input"]').type(password)
  cy.get('[data-cy="login-button"]').click()
})

// Comando para login usando sessão (mais performático)
Cypress.Commands.add('loginBySession', (email, password) => {
  cy.session([email, password], () => {
    cy.visit('/login')
    cy.get('[data-cy="email-input"]').type(email)
    cy.get('[data-cy="password-input"]').type(password)
    cy.get('[data-cy="login-button"]').click()
    cy.url().should('not.include', '/login')
  })
})

// Comando para verificar se está autenticado
Cypress.Commands.add('verifyAuthenticated', () => {
  cy.getCookie('auth_token').should('exist')
  cy.url().should('not.include', '/login')
})
"""

LOGIN_TESTS: str = """
// cypress/e2e/login.cy.js
import LoginPage from '../pages/LoginPage'

describe('Tela de Login', () => {
  beforeEach(() => {
    LoginPage.visit()
  })

  context('Login com sucesso', () => {
    it('deve fazer login com credenciais válidas', () => {
      cy.fixture('users').then((users) => {
        LoginPage.login(users.validUser.email, users.validUser.password)
        LoginPage.verifySuccessfulLogin()
      })
    })

    it('deve fazer login usando comando customizado', () => {
      cy.fixture('users').then((users) => {
        cy.login(users.validUser.email, users.validUser.password)
        cy.verifyAuthenticated()
      })
    })
  })

  context('Validações de erro', () => {
    it('deve exibir erro ao tentar login com credenciais inválidas', () => {
      cy.fixture('users').then((users) => {
        LoginPage.login(users.invalidUser.email, users.invalidUser.password)
        LoginPage.verifyErrorMessage('Email ou senha inválidos')
      })
    })

    it('deve exibir erro quando email está vazio', () => {
      cy.fixture('users').then((users) => {
        LoginPage.fillPassword(users.validUser.password)
        LoginPage.clickSubmit()
        LoginPage.verifyErrorMessage('Email é obrigatório')
      })
    })

    it('deve exibir erro quando senha está vazia', () => {
      cy.fixture('users').then((users) => {
        LoginPage.fillEmail(users.validUser.email)
        LoginPage.clickSubmit()
        LoginPage.verifyErrorMessage('Senha é obrigatória')
      })
    })

    it('deve exibir erro quando ambos campos estão vazios', () => {
      LoginPage.clickSubmit()
      LoginPage.verifyErrorMessage('Preencha todos os campos')
    })
  })

  context('Validações de interface', () => {
    it('deve verificar elementos visíveis na página', () => {
      LoginPage.elements.emailInput().should('be.visible')
      LoginPage.elements.passwordInput().should('be.visible')
      LoginPage.elements.submitButton().should('be.visible').and('be.enabled')
      LoginPage.elements.forgotPasswordLink().should('be.visible')
    })

    it('deve verificar placeholders dos campos', () => {
      LoginPage.elements.emailInput().should('have.attr', 'placeholder', 'Digite seu email')
      LoginPage.elements.passwordInput().should('have.attr', 'placeholder', 'Digite sua senha')
    })

    it('deve desabilitar botão durante envio do formulário', () => {
      cy.fixture('users').then((users) => {
        cy.intercept('POST', '/api/login', (req) => {
          req.reply({ delay: 1000, statusCode: 200 })
        })

        LoginPage.fillEmail(users.validUser.email)
        LoginPage.fillPassword(users.validUser.password)
        LoginPage.clickSubmit()

        LoginPage.elements.submitButton().should('be.disabled')
      })
    })
  })

  context('Navegação', () => {
    it('deve redirecionar para página de recuperação de senha', () => {
      LoginPage.elements.forgotPasswordLink().click()
      cy.url().should('include', '/forgot-password')
    })
  })
})
"""

SUPPORT_E2E: str = """
// cypress/support/e2e.js
import './commands'

// Configurações globais
Cypress.on('uncaught:exception', (err, runnable) => {
  // Evita que o teste falhe por erros não capturados
  return false
})

// Hook executado antes de cada teste
beforeEach(() => {
  // Limpar cookies e localStorage
  cy.clearCookies()
  cy.clearLocalStorage()
})
"""

# Dicionário com todos os exemplos
EXAMPLES = {
    "structure": PROJECT_STRUCTURE,
    "config": CYPRESS_CONFIG,
    "package": PACKAGE_JSON,
    "page": LOGIN_PAGE,
    "fixture": USERS_FIXTURE,
    "commands": CUSTOM_COMMANDS,
    "tests": LOGIN_TESTS,
    "support": SUPPORT_E2E,
}

EXAMPLE_PRMPT: str = "\n\n".join(EXAMPLES.values())