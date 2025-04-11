# frontend/Dockerfile
FROM nginx:1.27.4-alpine-slim

# Remove default configuration and copy our config if needed.
RUN rm /etc/nginx/conf.d/default.conf
# You can optionally add a custom Nginx configuration in nginx.conf
COPY nginx.conf /etc/nginx/conf.d/

# Copy the frontend files into the directory served by Nginx
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
