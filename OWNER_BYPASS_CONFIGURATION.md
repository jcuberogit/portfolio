# 🔧 Configurar Bypass para Dueño - Push Directo a Main

## 🎯 Objetivo
Permitir que solo el dueño (tú) pueda hacer push directo a `main`, mientras las reglas de protección se mantienen para otros usuarios.

## 📋 Pasos para Configurar

### 1. Ir a Configuración de Reglas
Ve a: **https://github.com/jcuberogit/portfolio/settings/rules**

### 2. Editar Regla para `main`

Busca la regla que aplica a `main` y haz clic en **"Edit"** o **"Add rule"** si no existe.

### 3. Configurar Bypass para Dueños

En la sección **"Bypass list"** o **"Allow specified actors to bypass"**:

1. ✅ Activa la opción: **"Allow specified actors to bypass"**
2. ✅ Selecciona: **"Repository owners"** o **"Repository admins"**
3. ✅ Guarda los cambios

### 4. Configuración Recomendada para `main`

**Reglas a mantener:**
- ✅ **Require pull request before merging** (para otros usuarios)
- ✅ **Block force pushes** (opcional, pero recomendado)
- ✅ **Require linear history** (opcional)

**Bypass para:**
- ✅ **Repository owners** (tú)
- ✅ **Repository admins** (si tienes admins)

### 5. Alternativa: Desactivar Reglas Temporalmente

Si necesitas hacer push ahora mismo:

1. Ve a: https://github.com/jcuberogit/portfolio/settings/rules
2. **Temporalmente desactiva** las reglas que bloquean:
   - "Restrict creations" → Desactivar
   - "Restrict updates" → Desactivar (o agregar bypass)
3. Haz tu push
4. Vuelve a activar las reglas

## 🚀 Después de Configurar

Una vez configurado el bypass, podrás hacer push directo:

```bash
cd /Users/jcubero/ParadigmStore/portfolio-repo
git push origin main
```

## 📝 Nota Importante

- Las reglas de protección seguirán aplicándose a otros usuarios
- Solo tú (y los que agregues al bypass list) podrán hacer push directo
- Los demás usuarios seguirán necesitando Pull Requests

## 🔗 Enlaces Directos

- **Configuración de Reglas**: https://github.com/jcuberogit/portfolio/settings/rules
- **Agregar Regla Nueva**: https://github.com/jcuberogit/portfolio/settings/rules/new

